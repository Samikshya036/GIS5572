-- Database: gis5572

-- DROP DATABASE IF EXISTS gis5572;

DROP TABLE feature_class_point;
-- Create Table for Point Data
CREATE TABLE feature_class_point (
    id SERIAL PRIMARY KEY,
    geom GEOMETRY (Point, 4326)
);
SELECT * FROM feature_class_point;

-- Insert 2 Points into the Table
INSERT INTO feature_class_point (geom)
VALUES 
    (ST_GeomFromText('POINT(-93.22773898145596 44.974068636239615)', 4326)),
    (ST_GeomFromText('POINT(-93.18973295365898 44.94326043904516)', 4326));

DROP TABLE feature_class_line;
-- Create Table for Line Data
CREATE TABLE feature_class_line (
    id SERIAL PRIMARY KEY,
    geom GEOMETRY(LineString, 4326)
);
-- Add coordinates to the line feature class
INSERT INTO feature_class_line (geom) VALUES
    (ST_SetSRID(ST_MakeLine(
        ST_MakePoint(-93.22773898145596, 44.974068636239615),
        ST_MakePoint(-93.18973295365898, 44.94326043904516)
    ), 4326));
SELECT * FROM feature_class_line;
DROP TABLE feature_class_polygon;
-- Create the polygon feature class
CREATE TABLE feature_class_polygon (
    id SERIAL PRIMARY KEY,
    geom GEOMETRY (Polygon, 4326)
);
Select * From feature_class_polygon;
Drop TABLE From feature_class_polygon;
-- Create the polygon feature class
CREATE TABLE feature_class_polygon (
    id SERIAL PRIMARY KEY,
    geom GEOMETRY (Polygon, 4326)
);

-- Add polygon to feature_class_polygon
INSERT INTO feature_class_polygon (geom)
VALUES
(
    ST_SetSRID(ST_GeomFromText('POLYGON((-93.22773898145596 44.974068636239615,
                                           -93.18973295365898 44.94326043904516,
                                           -93.17042775766252 44.988360414486756,
                                           -93.35274409842755 45.09143303212043,
                                           -93.22773898145596 44.974068636239615))'), 4326)
);

-- Select all records from feature_class_polygon to verify insertion
SELECT * FROM feature_class_polygon;
SELECT id, ST_AsText(geom) AS point_geometry FROM feature_class_point;
SELECT id, ST_AsText(geom) AS line_geometry FROM feature_class_line;
SELECT id, ST_AsText(geom) AS line_geometry FROM feature_class_polygon;
--view each row in an attribute
SELECT * FROM feature_class_point;
---- summarize the content
-- Count the total number of features in the feature class
SELECT COUNT(*) AS total_features FROM feature_class_point;
SELECT COUNT(*) AS total_features FROM feature_class_line;
SELECT COUNT(*) AS total_features FROM feature_class_polygon;


-- Define the name of your table
CREATE TABLE Sami_table (
    id SERIAL PRIMARY KEY,
    geom GEOMETRY (Polygon, 4326)
);


-