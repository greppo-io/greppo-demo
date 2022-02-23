from greppo import app
import ee
import os
email = os.environ['EE_EMAIL']
key_file = os.environ['EE_KEY_FILE']

# Authenticate and initialize
# email = "my-service-account@...gserviceaccount.com"
# key_file = "/path-to-key/key-file.json"
credentials = ee.ServiceAccountCredentials(email=email, key_file=key_file)
ee.Initialize(credentials)

# Select the satellite dataset from the catalog
dem = ee.Image('USGS/SRTMGL1_003')

# Process it
ee_dem = dem.updateMask(dem.gt(0))

# Provide visualisation parameters
vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

app.ee_layer(ee_object=ee_dem, vis_params=vis_params, name='DEM', description='World Digital Elevation Map from GEE')

app.display(name='text1', value='# Enter point value for finding its elevation')
lon = app.number(name='Longitude of the Point', value=86.9250)
lat = app.number(name='Latitude of the Point', value=27.9881)
point_name = app.text(name='Enter the name of point', value='Mt. Everest')

# Point object in EE
ee_point = ee.Geometry.Point([lon, lat])
app.ee_layer(ee_object=ee_point, vis_params={"color": "red"}, 
             name=point_name, description=f"The Point representing {point_name}.")

# Display the elevation
elev = ee_dem.sample(ee_point, 30).first().get('elevation').getInfo()

elev_text = f"""
# Elevation of point: {point_name}

## Point: (Lon: {lon}, Lat: {lat})
## Elevation: {elev}m
"""
text = f'## The elevation of point (Lon: {lon}, Lat: {lat}) is: {elev}m'
app.display(name='elev-text', value=elev_text)

app.map(center=[lat, lon], zoom=5)