import os
import pandas as pd
import geopandas as gpd

# Set the location of the Google application credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/mjumbewu/Code/musa/musa-509/lab-08-maps-and-charts-in-html/lab08-data-key.json'

# Query the map data table
df = pd.read_gbq('''
    SELECT name,
           st_astext(geometry) AS geometry_text,
           scaled_visit_count
    FROM lab08.corridor_map_data
''')

# Convert the results from a DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(
    df.drop('geometry_text', axis=1), geometry=gpd.GeoSeries.from_wkt(df.geometry_text))

# Output the GeoJSON representation of our GeoDataFrame
print(gdf.to_json())
