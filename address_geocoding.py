import geopy.geocoders as geoc


user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0"
geolocator = geoc.Nominatim(user_agent=user_agent)


address = "127 bainbridge street brooklyn"
address = "1908 3rd avenue manhattan"
loc = geolocator.geocode(address)



