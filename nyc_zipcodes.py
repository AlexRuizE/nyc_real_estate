"""Plot and process zip code data."""

import geopandas as gpd
import matplotlib.pyplot as plt


nycZips = "nyc_zipcodes/ZIP_CODE_040114.shp"
z = gpd.read_file(nycZips)