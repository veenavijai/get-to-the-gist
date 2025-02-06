from flask import Flask, render_template
import ee
import geemap

app = Flask(__name__)
ee.Authenticate()
ee.Initialize(project='ee-geodb')

@app.route('/')
def index():
    geojson_file_path = 'data/stateofwa.geojson'
    try:
      feature_collection = geemap.geojson_to_ee(geojson_file_path)
      Map = geemap.Map()

      print(ee.String('Successfully converted geoJSON to an EE feature collection').getInfo())

      # Center the map on the GeoJSON data
      Map.centerObject(feature_collection)

      Map.addLayer(feature_collection, {'color': 'red'}, 'GeoJSON Features')

      # Get the HTML code for the map
      map_html = Map.html  

      return render_template('index.html', map_html=map_html)

    # Return error message to the browser
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)