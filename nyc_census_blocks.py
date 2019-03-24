"""NYC census blocks"""

import geopandas as gpd
import matplotlib.pyplot as plt
%matplotlib qt5


dataDir='/home/monorhesus/Data/GIS/nyc_real_estate_data/'


# NYC
boros=gpd.read_file(dataDir+'nyc_boros.geojson')
boros['city']='nyc'
boros=boros.dissolve('city')
project_crs=boros.crs

# Blocks
nyblocks=gpd.read_file(dataDir+'nyc_census_blocks.geojson')
if not nyblocks.crs:
	nyblocks=nyblocks.to_crs(project_crs)

# plot
base = boros.plot(color='white', edgecolor='darkgray')
nyblocks.plot(ax=base, color='white', edgecolor='purple', alpha=.1)
plt.show()






