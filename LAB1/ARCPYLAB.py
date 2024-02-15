#import required libraries
#import arcpy


# Define workspace
work_directory = r"C:\Users\samik\OneDrive\Documents\ArcGIS\Projects\Samikshya1\Samikshya1.gdb"
arcpy.env.workspace = work_directory

# Define spatial reference (WGS 1984)
spatial_reference = arcpy.SpatialReference(4326)


# Create point feature class
point = "Featureclassp"
featureclass_point = arcpy.CreateFeatureclass_management(work_directory, point , "POINT", spatial_reference=spatial_reference)


# Adding points to the feature class
with arcpy.da.InsertCursor(featureclass_point, ["SHAPE@XY"]) as cursor:
    cursor.insertRow([(-93.22773898145596, 44.974068636239615)])
    cursor.insertRow([(-93.18973295365898, 44.94326043904516)])


# Create line feature class
line = "Featureclassl"
featureclass_line = arcpy.CreateFeatureclass_management(work_directory, line , "POLYLINE", spatial_reference=spatial_reference)


# Adding line to the feature class
with arcpy.da.InsertCursor(featureclass_line, ["SHAPE@"]) as cursor:
    array = arcpy.Array([arcpy.Point(-93.22773898145596, 44.974068636239615),
                         arcpy.Point(-93.18973295365898, 44.94326043904516)])
    polyline = arcpy.Polyline(array)
    cursor.insertRow([polyline])


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


# Step 8: View each row in an attribute table for a feature class
print("Attribute Table for Feature Class Point:")
with arcpy.da.SearchCursor(featureclass_point, "*") as cursor:
    for row in cursor:
        print(row)

print("Attribute Table for Feature Class Line:")
with arcpy.da.SearchCursor(featureclass_line, "*") as cursor:
    for row in cursor:
        print(row)

print("Attribute Table for Feature Class Polygon:")
with arcpy.da.SearchCursor(featureclass_polygon, "*") as cursor:
    for row in cursor:
        print(row)


# Step 9: View each geometry object in a feature class
print("Geometry Objects in Feature Class Point:")
with arcpy.da.SearchCursor(featureclass_point, "SHAPE@") as cursor:
    for row in cursor:
        print(row[0].JSON)

print("Geometry Objects in Feature Class Line:")
with arcpy.da.SearchCursor(featureclass_line, "SHAPE@") as cursor:
    for row in cursor:
        print(row[0].JSON)

print("Geometry Objects in Feature Class Polygon:")
with arcpy.da.SearchCursor(featureclass_polygon, "SHAPE@") as cursor:
    for row in cursor:
        print(row[0].JSON)


# Step 10: Summarize the contents of each feature class

# Function to summarize feature class
def summarize_feature_class(feature_class):
    # Get count of features
    feature_count = arcpy.GetCount_management(feature_class)
    print("Number of features in {}: {}".format(feature_class, feature_count))

# Summarize each feature class
summarize_feature_class(featureclass_point)
summarize_feature_class(featureclass_line)
summarize_feature_class(featureclass_polygon)


# Step 11: Export to shapefile

# Define output directory for shapefiles (same as the geodatabase location)
shapefile_output_directory = r"C:\Users\samik\OneDrive\Documents\ArcGIS\Projects\Samikshya1\Samikshya1.gdb"

# Export point feature class to shapefile
arcpy.FeatureClassToFeatureClass_conversion(featureclass_point, shapefile_output_directory, "Point_Shapefile")

# Export line feature class to shapefile
arcpy.FeatureClassToFeatureClass_conversion(featureclass_line, shapefile_output_directory, "Line_Shapefile")

# Export polygon feature class to shapefile
arcpy.FeatureClassToFeatureClass_conversion(featureclass_polygon, shapefile_output_directory, "Polygon_Shapefile")


# Step 11: Export to geodatabase

# Define output directory for geodatabase
gdb_output_directory = r"C:\Users\samik\OneDrive\Documents\ArcGIS\Projects\Samikshya1\Samikshya1.gdb"

# Export point feature class to geodatabase
arcpy.FeatureClassToFeatureClass_conversion(featureclass_point, gdb_output_directory, "Point_Feature")

# Export line feature class to geodatabase
arcpy.FeatureClassToFeatureClass_conversion(featureclass_line, gdb_output_directory, "Line_Feature")

# Export polygon feature class to geodatabase
arcpy.FeatureClassToFeatureClass_conversion(featureclass_polygon, gdb_output_directory, "Polygon_Feature")


# Step 12: Export WKT from file

# Define output file path for WKT
wkt_output_file = r"C:\Users\samik\OneDrive\Documents\ArcGIS\Projects\Samikshya1\wkt_output.txt"

# Function to write WKT to file
def write_wkt_to_file(feature_class, output_file):
    with open(output_file, "w") as file:
        # Open a search cursor to iterate through the geometries
        with arcpy.da.SearchCursor(feature_class, ["SHAPE@WKT"]) as cursor:
            for row in cursor:
                wkt = row[0]  # Get the WKT representation
                file.write(wkt + "\n")  # Write WKT to file

# Write WKT for each feature class to the output file
write_wkt_to_file(featureclass_point, wkt_output_file)
write_wkt_to_file(featureclass_line, wkt_output_file)
write_wkt_to_file(featureclass_polygon, wkt_output_file)

print("WKT has been exported to", wkt_output_file)

