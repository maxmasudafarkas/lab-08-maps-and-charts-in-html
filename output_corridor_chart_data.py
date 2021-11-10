import os
import pandas as pd

# Set the location of the Google application credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/mjumbewu/Code/musa/musa-509/lab-08-maps-and-charts-in-html/lab08-data-key.json'

# Query the chart data table
df = pd.read_gbq('''
    SELECT year || '-' || month || '-' || day as fulldate,
           visit_count
    FROM lab08.corridor_timeseries_data
''')

# Output the date values
print(list(df.fulldate))
print()

# Output the count values
print(list(df.visit_count))
print()
