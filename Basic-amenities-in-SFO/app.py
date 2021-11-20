from greppo import app
import geopandas as gpd

sfo_amenities = gpd.read_file("./SFO_Amenities.geojson")
amenities = list(sfo_amenities['amenity'].unique())

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

default_area_selection = gpd.read_file("./SFO_Selection.geojson")
area_selection = app.draw_feature(
    name="Draw area selection", features=default_area_selection, geometry=["Polygon"]
)

selected_amenities = sfo_amenities.loc[sfo_amenities.within(
    area_selection.at[0, 'geometry'])]
selected_amenities_count_df = selected_amenities['amenity'].value_counts()

selected_amenities_count = []

for amenity in amenities:
    if(amenity in selected_amenities_count_df.index):
        selected_amenities_count.append(
            selected_amenities_count_df[amenity].item())
    else:
        selected_amenities_count.append(0)

app.bar_chart(
    name="amenities-sfo-select",
    title="Amenities in SFO",
    description="The count of the basic amenities within the selected area in SFO.",
    x=amenities,
    y=selected_amenities_count,
    backgroundColor="rgb(200, 50, 150)",
)
