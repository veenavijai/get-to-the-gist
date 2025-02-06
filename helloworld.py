import ee

ee.Authenticate()
ee.Initialize(project='ee-geodb')
print(ee.String('Hello from the Earth Engine servers!').getInfo())