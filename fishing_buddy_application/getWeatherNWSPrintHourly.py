import json
import requests
import datetime

class Weather:

  def printFutureWeatherResults(self, weatherData, numberFutureHours):
    #self.theWeatherJSON = json.loads(weatherData)
    self.theWeatherJSON = weatherData
    self.printNumberOfHours = numberFutureHours

    self.startDateYearMonthDay = datetime.datetime.strptime(self.theWeatherJSON["properties"]["periods"][0]["startTime"], '%Y-%m-%dT%H:%M:%S%z')

    print(self.startDateYearMonthDay.strftime("%B %d %Y") + " weather report for the next " + str(self.printNumberOfHours) + " hours:")
    # for each hourly period, print the temp, wind where it occurred
    #for i in theWeatherJSON["properties"]["periods"]:
    for i in range(self.printNumberOfHours):
      self.weatherSubsetJSON = self.theWeatherJSON["properties"]["periods"][i]

      print("------------------------------")
      #print (i["startTime"].strftime("%I:%M:%S %p") + " to " + i["endTime"].strftime("%I:%M:%S %p"))
      startTimeOriginal = self.weatherSubsetJSON["startTime"]
      #print("the original start time is")
      #print(i["startTime"])
      #"startTime": "2021-01-10T01:00:00-06:00",
      startTimeFormatted = datetime.datetime.strptime(startTimeOriginal, '%Y-%m-%dT%H:%M:%S%z')
      endTimeOriginal = self.weatherSubsetJSON["endTime"]
      #"endTime": "2021-01-10T02:00:00-06:00",
      endTimeFormatted = datetime.datetime.strptime(endTimeOriginal, '%Y-%m-%dT%H:%M:%S%z')

      #print(startTimeFormatted)
      #print(endTimeFormatted)
      print("Time: " + startTimeFormatted.strftime("%I:%M %p") + " to " +  endTimeFormatted.strftime("%I:%M %p"))
      print("Temp: " + str(self.weatherSubsetJSON["temperature"]) + " " + str (self.weatherSubsetJSON["temperatureUnit"]))
      print("Wind: " + str(self.weatherSubsetJSON["windDirection"]) + " at " + str (self.weatherSubsetJSON["windSpeed"]))
  

# User-Agent: (myweatherapp.com, contact@myweatherapp.com)
headers = {'user-agent': 'JeremiahBrooks, jbullfrog81@gmail.com'}

nwsAPIEndPointFull = "https://api.weather.gov/points/39.7456,-97.0892/forecast/hourly"

#req = requests.get(nwsAPIEndPointFull, headers=headers)
#theJSON = req.json()
#print(req.json())
with open('./sampleWeatherData.json') as f:
  theJSON = json.load(f)

printNumberFutureHours = 6
weatherResults = Weather()
weatherResults.printFutureWeatherResults(theJSON,printNumberFutureHours)
#print(req.json())
