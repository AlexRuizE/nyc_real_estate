# NYC Real Estate

Scripts (mostly python) to retrieve, update, process and visualize NYC real estate data from multiple official and secondary sources. It contains the following files:

* __data-io.py__: Classes to get/put data from local <> remote.

* __nyc_sales_scrape_monthly.py__: Recurrent (monthly) update of the rolling real estate sales data provided by the Department of Finance on NYC. Must be run monthly to update the resulting dataframe.

* __nyc_nyu_historical.py__: Script to process geotagged historical real estate sales data in NYC, as provided by NYU.

* __exploratory_nyc_nyu_historical.py__: Initial script to explore the structure, contents and usability of geotagged data provided by NYU. Files containing the keyworkd _exploratory_ will eventually be moved to its own __sandbox__ directory.


* __nyc_zipcodes.py__: Script to load and process NYC zipcodes polygon data.

* __nyc_zipcodes__: Directory with zipcodes polygon data. All data files will eventually be moved to S3.
