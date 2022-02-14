from greppo import app
import geopandas as gpd

app.base_layer(
    name="CartoDB Light",
    visible=True,
    url="https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
    subdomains=None,
    attribution='&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors | Carto Tile',
)

regions = gpd.read_file("./regions.geojson")
roads = gpd.read_file("./roads.geojson")
cities = gpd.read_file("./cities.geojson")

app.overlay_layer(
    regions,
    name="Regions of Italy",
    description="Polygons showing the boundaries of regions of Italy.",
    style={"fillColor": "#74c476"},
    visible=True,
)

app.overlay_layer(
    roads,
    name="Highways in Italy",
    description="Lines showing the major highways in Italy.",
    style={"fillColor": "#6a51a3"},
    visible=True,
)

app.overlay_layer(
    cities,
    name="Cities of Italy",
    description="Points showing the cities in Italy.",
    style={"fillColor": "#de2d26"},
    visible=True,
)