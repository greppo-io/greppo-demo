from greppo import app
import geopandas as gpd

some_text = """
### Display selected count of amenities in SFO

This app counts the different amenities within the drawn polygon on the map, and displays the data on a chart below.
"""
app.display(value=some_text, name="some-text")

app.base_layer(
    provider="OpenStreetMap Mapnik",
)

sfo_amenities = gpd.read_file("./SFO_Amenities.geojson")

app.overlay_layer(
   sfo_amenities,
   name="SFO Amenities",
   description="Location of some basic amenities in San Francisco",
   style={"fillColor": "#F87979"},
   visible=True,
)

default_area_selection = gpd.read_file("./SFO_Selection.geojson")
# default_area_selection = gpd.GeoDataFrame({'geometry' : []}, crs="EPSG:4326")

area_selection = app.draw_feature(
   name="Draw area selection", features=default_area_selection, geometry=["Polygon"]
)

amenities = list(sfo_amenities['amenity'].unique())
selected_amenities_count = dict.fromkeys(amenities, 0)
for idx, row in area_selection.iterrows():
   selected_amenities = sfo_amenities.loc[sfo_amenities.within(
       row.at['geometry'])]
   selected_amenities_count_df = selected_amenities['amenity'].value_counts()
   for amenity in amenities:
       if(amenity in selected_amenities_count_df.index):
           selected_amenities_count[amenity] = selected_amenities_count[amenity] + \
               selected_amenities_count_df[amenity].item()

barX = list(selected_amenities_count.keys())
barY = list(selected_amenities_count.values())

app.line_chart(
   name="amenities-sfo-select",
   description="The count of the basic amenities within the selected area in SFO.",
   x=barX,
   y=barY,
   backgroundColor="rgb(200, 50, 150)",
)


