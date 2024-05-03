import psycopg2
from flask import Flask
import os


# create the Flask app
app = Flask(__name__) 

# Connect to the PostgreSQL database

# create the index route
@app.route('/') 
def index(): 
    return "The API is working!"

# create a general DB to GeoJSON function
def database_to_geojson(table_name):
        # create connection to the DB
    conn = psycopg2.connect(
        host = os.environ.get("34.31.152.38"),
        database = os.environ.get("gis5572"),
        user = os.environ.get("postgres"),
        password = os.environ.get("sami@2010"),
        port = os.environ.get("5432"),
    )
    # retrieve the data
    with conn.cursor() as cur:
        query =f"""
        SELECT JSON_BUILD_OBJECT(
            'type', 'FeatureCollection',
            'features', JSON_AGG(
                ST_AsGeoJson({table_name}.*)::json
            )
        )
        FROM {table_name};
        """
        
        cur.execute(query)
        
        data = cur.fetchall()
    # close the connection
    conn.close()
    
    # Returning the data
    return data [0][0]

# create the data route

@app.route('/get_agdd_20235_20239', methods=['GET'])
def get_et_idw_geojson():
    # call our general function
    agdd_idw = database_to_geojson("et2023_idw_point")
    return et_idw

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
