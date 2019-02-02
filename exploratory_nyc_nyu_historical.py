"""EXPLORATORY Script to process and manage historical data of NYC real estate sales. Uses geotagged data provided by the 
NYC Geocoded Real Estate Sales project of the Newman Library (Bernard M. Baruch College), NYU.
Seems like shape files are being deprecated and sqlite dataframes are being used moving forward."""

import os
import geopandas as gpd
from sqlite3 import dbapi2 as sqlite
import matplotlib.pyplot as plt
# %matplotlib

# Env Vars
dataDir = "/home/monorhesus/Data/GIS/nyc_real_estate_data/nyc_realestate_sales/"
nycZips = "nyc_zipcodes/ZIP_CODE_040114.shp"

############
# Zipcodes #
############nycZips = "nyc_zipcodes/ZIP_CODE_040114.shp"
z = gpd.read_file(nycZips)

###############
# Shape files #
###############
shapeFiles = [file for file in os.listdir(dataDir) if ".shp" in file]
shapeFiles.sort()
sales = gpd.pd.DataFrame()
base_x,base_y = 6.4,4.8
expansion_f = 1.8
figsize=(base_x*expansion_f, base_y*expansion_f)
    

# Single year
file=shapeFiles[-1]
sales = gpd.read_file(dataDir+file)
c=['price','address', 'apt','zip', 'res_unit', 'com_unit']
c1=[col for col in sales.columns if col not in ('geometry', 'Sale_id')]

sales[(sales.usable=="N") & (sales.price>100)]

for file in shapeFiles:
	year = file.split("_")[-1].split(".")[0]
	print(f"Loading {file}")
	salesTemp = gpd.read_file(dataDir+file)
	salesTemp["year"] = year
	sales = sales.append(salesTemp)
	print("Plotting {}".format(file))
	base = z.plot(color='white', edgecolor='darkgray', figsize=figsize)
	salesTemp.plot(ax=base, marker='o', color='red', alpha=.5 ,markersize=.05, label=year, figsize=figsize)
	plt.legend(frameon=False, fontsize=15)
	plt.savefig("plots/"+year+".png")
	plt.close()





sales.plot(markersize=.05) # (1247356, 30)


##########
# Sqlite #
##########
#Method 1


# #Method 2
# sharedLib = "/usr/lib/libspatialite.so"
# sqliteFile = "NYC_RealEstate_Sales_2003_2015.sqlite"
# con = sqlite.connect(dataDir+sqliteFile)
# con.enable_load_extension(True)
# con.execute("select load_extension('{}');".format(sharedLib))



