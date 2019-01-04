"""Script to process and manage historical data of NYC real estate sales. Uses geotagged data provided by the 
NYC Geocoded Real Estate Sales project of the Newman Library (Bernard M. Baruch College), NYU.
Seems like shape files are being deprecated and sqlite dataframes are being used moving forward."""

import os
import geopandas as gpd
from sqlite3 import dbapi2 as sqlite
%matplotlib

# Env Vars
dataDir = "/home/monorhesus/Data/GIS/nyc_real_estate_data/nyc_realestate_sales/"

#TODO: Explore data 
