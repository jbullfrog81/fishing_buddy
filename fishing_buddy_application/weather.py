import json
import requests
import datetime

class Weather:

  def printFutureWeatherResults(self, weatherData, numberFutureHours):
    #Set add the JSON dataset from object instance argument weatherData (should be JSON) to the local object instance theWeatherJSON
    self.theWeatherJSON = weatherData

    #Set the number of future hours of weather data from incoming object instance argument numberFutureHours to the local object instance futureWeatherNumberOfHours
    self.futureWeatherNumberOfHours = numberFutureHours

    #Set the start of the weather data's year month day and time from the JSON dataset. This converts it to python date time to be manipulated in the future.
    #Example of the raw JSON data format before converted to Python datatime:
    #2021-01-03T20:00:00-06:00
    self.startDateYearMonthDay = datetime.datetime.strptime(self.theWeatherJSON["properties"]["periods"][0]["startTime"], '%Y-%m-%dT%H:%M:%S%z')

    #Print out a header of the Month Day Year along with the number of hours included in the report
    #Example output:
    #January 03 2021 weather report for the next 6 hours:
    print(self.startDateYearMonthDay.strftime("%B %d %Y") + " weather report for the next " + str(self.futureWeatherNumberOfHours) + " hours:")

    #Loop through the JSON dataset of future weather based on how many hours was passed in through local object instance futureWeatherNumberOfHours
    #Print out the hourly future temperature, wind speed and wind direction
    #Example output:
    #January 03 2021 weather report for the next 6 hours:
    #------------------------------
    #Time: 02:00 PM to 03:00 PM
    #Temp: 45 F
    #Wind: SW at 10 mph
    #------------------------------
    #Time: 03:00 PM to 04:00 PM
    #Temp: 46 F
    #Wind: SW at 10 mph
    for i in range(self.futureWeatherNumberOfHours):
      #Set local object instance of the hours future weather
      self.weatherSubsetJSON = self.theWeatherJSON["properties"]["periods"][i]

      #print a divider for each hour for easy readability
      print("------------------------------")

      #Set the start time of the hourly weather dataset
      #Example data:
      #2021-01-10T01:00:00-06:00
      startTimeOriginal = self.weatherSubsetJSON["startTime"]

      #Set and convert start timestamp of hourly data to a python datetime format
      startTimeFormatted = datetime.datetime.strptime(startTimeOriginal, '%Y-%m-%dT%H:%M:%S%z')

      #Set the end time of the hourly weather dataset
      #Example data:
      #2021-01-10T02:00:00-06:00
      endTimeOriginal = self.weatherSubsetJSON["endTime"]

      #Set and convert start timestamp of hourly data to a python datetime format
      endTimeFormatted = datetime.datetime.strptime(endTimeOriginal, '%Y-%m-%dT%H:%M:%S%z')

      #Print out easy to read information for the hour of time, tempterature, wind speed and wind direction
      #Example output:
      #Time: 02:00 PM to 03:00 PM
      #Temp: 45 F
      #Wind: SW at 10 mph
      print("Time: " + startTimeFormatted.strftime("%I:%M %p") + " to " +  endTimeFormatted.strftime("%I:%M %p"))
      print("Temp: " + str(self.weatherSubsetJSON["temperature"]) + " " + str (self.weatherSubsetJSON["temperatureUnit"]))
      print("Wind: " + str(self.weatherSubsetJSON["windDirection"]) + " at " + str (self.weatherSubsetJSON["windSpeed"]))


#Set the request header with a user-agent field.
#This is required for authentication of the request by the National Weather Service API.
#Documentation says in the future the user-agent field to be replaced by API key but no known date
#Documentation at https://www.weather.gov/documentation/services-web-api
#Excerpt from National Weather Service API documentation around authentication:
#Authentication
#A User Agent is required to identify your application. This string can be anything, and the more unique to your application the less likely it will be affected by a security event.
#If you include contact information (website or email), we can contact you if your string is associated to a security event.
#This will be replaced with an API key in the future.
headers = {'user-agent': 'JeremiahBrooks, jbullfrog81@gmail.com'}

#Set the based end point for the National Weather Service API
nwsAPIEndPointBase = "https://api.weather.gov"

#set the URI section for the Hourly Forecast
nwsAPIHourlyForecastURI = "forecast/hourly"

#Set the geoloaction coordinates
geoLocationCoordinates = "39.7456,-97.0892"

#Set the full National Weather Service API endpoint
#Example:
#https://api.weather.gov/points/39.7456,-97.0892/forecast/hourly
nwsAPIEndPointFull = nwsAPIEndPointBase + "/points/" + geoLocationCoordinates + "/" + nwsAPIHourlyForecastURI

#Create request to the National Weather Service API endpoint to obtain the weather data
req = requests.get(nwsAPIEndPointFull, headers=headers)

if req.ok:
  theJSON = req.json()
  #debug option to print out the JSON request data
  #print(req.json())

  #Set the number of future hours of weather to display
  printNumberFutureHours = 6

  #Instantiate the class weather
  weatherResults = Weather()

  #Call the method to print the future weather results based on JSON data obtained from National Weather Service API
  weatherResults.printFutureWeatherResults(theJSON,printNumberFutureHours)
else:
  print("There was an error status code " + str(req.status_code) + " returned from end point " + nwsAPIEndPointFull)


#Utilize local file for testing code
#with open('./sampleWeatherData.json') as f:
#  theJSON = json.load(f)

#Set the number of future hours of weather to display
#printNumberFutureHours = 6

#Instantiate the class weather
#weatherResults = Weather()

#Call the method to print the future weather results based on JSON data obtained from National Weather Service API
#weatherResults.printFutureWeatherResults(theJSON,printNumberFutureHours)
