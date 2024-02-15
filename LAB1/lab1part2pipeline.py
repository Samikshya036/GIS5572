!pip install psycopg2-binary

import arcpy
work_directory = r'C:\Users\samik\OneDrive\Documents\ArcGIS\Projects\Lab1part2\Lab1part2.gdb'
arcpy.env.workspace = work_directory

# Define spatial reference (WGS 1984)
spatial_reference = arcpy.SpatialReference(4326)
# Create polygon feature class
polygon = "Featureclasspg"
featureclass_polygon = arcpy.CreateFeatureclass_management(work_directory, polygon , "POLYGON", spatial_reference=spatial_reference)


!pip install --force-reinstall psycopg2-binary


import psycopg2
import requests
import json
import os
from arcgis.gis import GIS
import re



# Create polygon feature class
polygon = "Featureclasspg"
featureclass_polygon = arcpy.CreateFeatureclass_management(work_directory, polygon , "POLYGON", spatial_reference=spatial_reference)


# Adding polygon to the feature class
with arcpy.da.InsertCursor(featureclass_polygon, ["SHAPE@"]) as cursor:
    array = arcpy.Array([arcpy.Point(-93.22773898145596, 44.974068636239615),
                        arcpy.Point(-93.18973295365898, 44.94326043904516),
                        arcpy.Point(-93.17042775766252, 44.988360414486756), 
                        arcpy.Point(-93.35274409842755, 45.09143303212043)])
    polygon = arcpy.Polygon(array)
    cursor.insertRow([polygon])

# Retrieve WKT representation of the inserted polygon
with arcpy.da.SearchCursor(featureclass_polygon, ["SHAPE@WKT"]) as cursor:
    for row in cursor:
        wkt_polygon = row[0]
        print(wkt_polygon)

# Original MULTIPOLYGON WKT string
wkt_mp = "MULTIPOLYGON (((-93.227722167999957 44.974121094000054, -93.189697265999939 44.943298340000069, -93.170410155999946 44.988281250000057, -93.352722167999957 45.091491699000073, -93.227722167999957 44.974121094000054)))"

# Convert MULTIPOLYGON to POLYGON (simple case)
wkt_p = wkt_mp.replace("MULTIPOLYGON (((", "POLYGON ((").replace(")))", "))")

print("Converted WKT representation:")
print(wkt_p)


### Connect to PostGRE sql

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="34.31.152.38",
    database="gis5572",
    user="postgres",  # Replace "your_username" with your actual username if required
    password="%",
    port="5432"
)


# Define your SQL query to insert the polygon into the database
sql = f"INSERT INTO Sami_table (geom) VALUES (ST_GeomFromText('{wkt_p}', 4326))"


try:
    # Execute the SQL query
    cur.execute(sql)
    
    # Commit the transaction
    conn.commit()
    
    print("Polygon inserted successfully.")
except Exception as e:
    # Rollback the transaction if an error occurs
    conn.rollback()
    print("Error inserting polygon:", e)

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()





# Your API endpoint
api = 'http://35.202.218.119:5000/get_polygon'

try:
    response = requests.get(api)
    response.raise_for_status()
    dictionary = json.loads(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error during API request: {e}")
    exit()


# Check if 'features' key exists
if 'features' in dictionary and len(dictionary['features']) > 0:
    # Extract geometry from the first feature
    geometry_str = dictionary['features'][0]['geometry']

    # Replace multiple occurrences using a regular expression
    geometry_str = re.sub(r'\[\[\[\[\[', '[[[', geometry_str)
    geometry_str = re.sub(r'\]\]\]\]\]', ']]]', geometry_str)

    try:
        # Parse the cleaned geometry string into a dictionary
        geometry_dict = json.loads(geometry_str)
        print(geometry_dict)
    except json.JSONDecodeError as e:
        print(f"Error decoding geometry string: {e}")
else:
    print("Error: 'features' key not found or empty in the API response.")

# Specify GeoJSON dictionary name and then create
path = os.path.join(r'C:\Users\samik\OneDrive\Documents\ArcGIS\Projects\Lab1part2', 'Lab1geojson.json')
Lab1geojson = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": geometry_dict['coordinates'],
        "type": "Polygon"
      }
    }
  ]
}

# Use raw string (r'') for Windows paths to handle backslashes

# Use 'with' statement for file handling to ensure proper closing
with open(path, 'w') as json_file:
    json.dump(Lab1geojson, json_file, indent=2)  # Indent for better readability
     

username = 'username'
password = '$'
gis = GIS('https://www.arcgis.com', username, password)
print("Successfully signed in to ArcGIS Online.")


