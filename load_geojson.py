import ee
import geemap

ee.Initialize(project='ee-geodb')

geojson_file_path = 'data/stateofwa.geojson'

try:
    feature_collection = geemap.geojson_to_ee(geojson_file_path)

    print(feature_collection.size().getInfo())

except Exception as e:
    print(f"Error importing GeoJSON: {e}")

Map = geemap.Map()

# Center the map
Map.centerObject(feature_collection) 

Map.addLayer(feature_collection, {'color': 'red'}, 'GeoJSON Features')

# TODO Display the map in the default web browser
Map

print(ee.String('Successfully converted geoJSON to an EE feature collection').getInfo())