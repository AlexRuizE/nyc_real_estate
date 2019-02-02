"""Plot and process zip code data."""

import geopandas as gpd
%matplotlib

nycZips = "nyc_zipcodes/ZIP_CODE_040114.shp"  
z = gpd.read_file(nycZips)

z.plot(color='white', edgecolor='darkgray')
