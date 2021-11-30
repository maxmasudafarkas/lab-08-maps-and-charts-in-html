# HTML with Maps and Charts

In this lab you're going to create a simple HTML page and populate it with some text, a map, and a chart. The data for the map and chart are going to come from a BigQuery dataset that I've created. The file `lab08-data-key.json` in this folder contains a Google service account key that can be used to access the data.

We are going to use [Leaflet](https://leafletjs.com/) to map our data, and [C3](https://c3js.org/) to create a timeseries chart.

1. In an environment, install the following packages:

   * geopandas
   * pandas-gbq

geopandas install: conda install --channel conda-forge geopandas
pandas-gbq install: pip install pandas-gbq -U

1. Create an `index.html` file

1. Set up the basic structure of your HTML page. Every HTML document has a **head** and a **body**. Create a file called `index.html` and add the following.

   ```html
   <html>
       <head>
           <title></title>
       </head>
       <body>

       </body>
   </html>
   ```

1. In your body, add a level-1 heading (`h1`) element with the content `Philadelphia Commercial Corridor Data`.

1. In your body, add two paragraph (`p`) elements, one with the content `The following map shows the amount of traffic in each commercial corridor.` and another with the content `The following chart shows the amount of traffic to all corridors over time.`.

1. In your body, add two `div` elements, one with an `id` of `"map"` and the other with an `id` of `"chart"`.

1. Add the style sheet for Leaflet to your page. In your head, add the following element (pulled from the [Leaflet Quick Start Guide](https://leafletjs.com/examples/quick-start/)):

   ```html
   <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
    integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
    crossorigin=""/>
   <style>
     #map {
       height: 250px;
     }
   </style>
   ```

1. Add the JavaScript library for Leaflet to your page. At the bottom of your body, add the following element (pulled from the [Leaflet Quick Start Guide](https://leafletjs.com/examples/quick-start/)):

   ```html
   <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
    integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
    crossorigin=""></script>
   ```

1. Add the following script element to the bottom of your body. This will add a map into the element with ID `map`:

   ```html
   <script>
   var map = L.map('map').setView([40, -75.2], 11);
   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
       attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
   }).addTo(map);

   var mapdata = {};
   var colors = d3.interpolate("red", "green");
   L.geoJSON(mapdata, {
     style: (feature) => {
       return {
         fillColor: colors(feature.properties.scaled_visit_count),
         weight: 1,
         color: 'black',
         fillOpacity: 0.9
       }
     }
   }).addTo(map);
   </script>
   ```

   > Note that the above uses OpenStreetMap base tiles, but you can use any base tiles you want. For example, the [Stamen](http://maps.stamen.com/) tiles are a popular free alternative. If we have time toward the end of the semester, we may look into creating custom base tiles with [Mapbox](https://mapbox.com/) as well.

1. Add the style sheet for C3 to your page. In your head, add the following element (pulled from the [The cdnjs page for C3](https://cdnjs.com/libraries/c3)):

   ```html
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.20/c3.min.css"
    integrity="sha512-cznfNokevSG7QPA5dZepud8taylLdvgr0lDqw/FEZIhluFsSwyvS81CMnRdrNSKwbsmc43LtRd2/WMQV+Z85AQ=="
    crossorigin="anonymous" referrerpolicy="no-referrer" />
   ```

1. Add the JavaScript libraries for C3 and D3 to your page. At the bottom of your body, add the following element (pulled from the the cdnjs pages for [C3](https://cdnjs.com/libraries/c3) and [D3](https://cdnjs.com/libraries/d3/5.16.0) respectively):

   ```html
   <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/5.16.0/d3.min.js"
    integrity="sha512-FHsFVKQ/T1KWJDGSbrUhTJyS1ph3eRrxI228ND0EGaEp6v4a/vGwPWd3Dtd/+9cI7ccofZvl/wulICEurHN1pg=="
    crossorigin="anonymous" referrerpolicy="no-referrer"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/c3/0.7.20/c3.min.js"
    integrity="sha512-+IpCthlNahOuERYUSnKFjzjdKXIbJ/7Dd6xvUp+7bEw0Jp2dg6tluyxLs+zq9BMzZgrLv8886T4cBSqnKiVgUw=="
    crossorigin="anonymous" referrerpolicy="no-referrer"></script>
   ```

1. Add the following script element to the bottom of your body. This will add a chart into the element with ID `chart`:

   ```html
   <script>
   var chartdates = [];
   var chartvalues = [];
   var chart = c3.generate({
     bindto: '#chart',
     data: {
       x: 'x',
       columns: [
         ['x', ...chartdates],
         ['Count', ...chartvalues]
       ]
     },
     axis: {
       x: {
         type: 'timeseries'
       }
     }
   });
   </script>
   ```

1. Run the `output_corridor_map_data.py` script to get GeoJSON data that we can put on our map. On the line that says `var mapdata = {};`, replace the `{}` with the data output by the script. _Tip: You can output the data to a file by running:

```bash
python output_corridor_map_data.py > mapdata.json
```

The `> mapdata.json` at the end of that line will dump whatever would normally be output to the terminal screen from the `python output_corridor_map_data.py` command into a file named `mapdata.json`

1. Run the `output_corridor_chart_data.py` script to get arrays of values for the chart. On the line in your HTML that says `var chartdates = [];`, replace the `[]` with the first line of data output from the script, and on the line that says `var chartvalues = [];` replace the `[]` with the second line of output from the script.
