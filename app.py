from greppo import app
import geopandas as gpd

sfo_amenities = gpd.read_file("./datasets/SFO_Amenities.geojson")

app.base_layer(
    name="CartoDB Light",
    visible=True,
    url="https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
    subdomains=None,
    attribution='&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors | Carto Tile',
)

app.overlay_layer(
    sfo_amenities,
    title="SFO Amenities",
    description="Location of some basic amenities in San Francisco",
    style={"fillColor": "#F87979"},
    visible=True,
)

area_selection = gpd.read_file("./datasets/SFO_Selection.geojson")
draw_feature_polygon = app.draw_feature(
    name="Draw area selection", features=area_selection, geometry=["Polygon"]
)

selected_amenities = sfo_amenities[sfo_amenities.within(area_selection)]


