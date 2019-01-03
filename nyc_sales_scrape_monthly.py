"""Script to update monthly NYC sales data (nyc.gov)."""

import requests
import bs4
import pandas as pd

# Variables
homeUrl = "https://www1.nyc.gov"
salesUrl = "/site/finance/taxes/property-rolling-sales-data.page"
dataDir = "/home/monorhesus/Dropbox/codigo/data/nyc_rolling_sales/"


# Get borough sales urls
mainPage = requests.get(homeUrl+salesUrl)
assert mainPage.ok, "Could not get main sales page. "
html = bs4.BeautifulSoup(mainPage.text, "lxml")
htmlTable = html.find("table")
links = [link.get("href") for link in htmlTable.find_all("a")]
links = [link for link in links if ".xls" in link]
dataLinks = [homeUrl+link for link in links]

# Get data
fileNames=[]
for link in dataLinks:
	fileName = link.split("/")[-1]
	fileNames.append(fileName)
	getData = requests.get(link)
	if getData.ok:
		with open(dataDir+"nycgov_raw/"+fileName, "wb") as f:
			f.write(getData.content)
			print("Saved {} in {}".format(link, dataDir))
	else:
		print("Link {} not retreived.".format(link))

# Update dataframe
skipRows=4
df = pd.DataFrame()
for file in fileNames:
	dfTemp = pd.read_excel(dataDir+file, skiprows=skipRows)
	df = df.append(dfTemp)
df.columns = [col.lower().replace(" ","_") for col in df.columns]
df = df.reset_index(drop=True)

# Save update dataframe
df.to_csv(dataDir+"nycgov_sales_historic.csv", index=False)
# TODO: Update incrementally with monthly calls to this same site.

  

