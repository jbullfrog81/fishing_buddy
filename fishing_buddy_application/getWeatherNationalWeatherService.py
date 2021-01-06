import requests
#import nwswx
#
#nws = nwswx.WxAPI('jbullfrog81@gmail.com')
#forecast = nws.point_forecast(38.9056095, -94.7476295)
#print(forecast)


# User-Agent: (myweatherapp.com, contact@myweatherapp.com)
headers = {'user-agent': 'JeremiahBrooks, jbullfrog81@gmail.com'}

#https://api.weather.gov/points/39.7456,-97.0892

nwsAPIEndPoint = "https://api.weather.gov"
nwsAPIEndPointFull = "https://api.weather.gov/points/39.7456,-97.0892/forecast/hourly"

req = requests.get(nwsAPIEndPointFull, headers=headers)
print(req.json())
