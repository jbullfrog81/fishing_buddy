
##
#
#
#set all of the unique attributes about a Fishing Trip
from dataclasses import dataclass, field
import datetime

#@dataclass
class fishingTrip:
    
    date: str = "No date defined"
    startTime: int = 0
    endTime: int = 0
    lake: str = "No lake defined"
    waterTemp: int = 0
    fishCaught: int = 0
    airTemp: int = 0
    windSpeed: int = 0
    windDirection: str = "No wind defined"
    tripName: str = "No trip name defined"

    #def createNewFishingTrip(self,date,startTime,endTime,lake,airTemp,windSpeed,windDirection,waterTemp,fishCaught):   
        
    def __init__(self, date, startTime, endTime, lake, airTemp, windSpeed, windDirection, waterTemp, fishCaught):
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.lake = lake
        self.waterTemp = waterTemp
        self.fishCaught = fishCaught
        self.airTemp = airTemp
        self.windSpeed = windSpeed
        self.windDirection = windDirection
        
        #set a name for the trip
        tripName = ("trip - " + str(date) + str(startTime) + str(lake))
    
    def getFishingTripInformation(self):

        print("The trip information for " + str(self.tripName) + ": \n" + 
        "Date: " + str(self.date) + "\n" + 
        "Start Time: " + str(self.startTime) + "\n" + 
        "End time: " + str(self.endTime) + "\n" + 
        "on lake: " + str(self.lake) + "\n" + 
        "with water temperature:" + str(self.waterTemp) + "\n" + 
        "caught " + str(self.fishCaught) + " fish" + "\n" + 
        "air temperature of: " + str(self.airTemp) + "farenheight" + "\n" + 
        "wind blowing at " + str(self.windSpeed) + "mph" + "\n" + 
        "out of the " + str(self.windDirection)
        )

class fish:


class weather:


class lake:


def main():

    #date1 = "10/31/2020"
    date1 = datetime.date(2020, 10, 31)
    startTime1 = "10:00"
    endTime1 = "14:00"
    lake1 = "Hillsdale"
    waterTemp1 = 67
    fishCaught1 = 11
    airTemp1 = 56
    windSpeed1 = 11
    windDirection1 = "West"
    
    #print("**DEBUG** The trip information for trip: \n" + 
    #    "Date: " + str(date1) + "\n" + 
    #    "Start Time: " + str(startTime1) + "\n" + 
    #    "End time: " + str(endTime1) + "\n" + 
    #    "on lake: " + str(lake1) + "\n" + 
    #    "with water temperature:" + str(waterTemp1) + "\n" + 
    #    "caught " + str(fishCaught1) + " fish  caught " + "\n" + 
    #    "air temperature of: " + str(airTemp1) + " degrees farenheight" + "\n" + 
    #    "wind blowing at " + str(windSpeed1) + " mph" + "\n" + 
    #    "out of the " + str(windDirection1)
    #    )

    #build the first trip
    t1 = fishingTrip(date=date1, startTime=startTime1, endTime=endTime1, lake=lake1, waterTemp=waterTemp1, fishCaught=fishCaught1, airTemp=airTemp1, windSpeed=windSpeed1, windDirection=windDirection1)
    print("**DEBUG** The date of the fishing trip is:" + str(t1.date))


    #b1.addchapter(Chapter("Chapter 1", 104))
    #b1.addchapter(Chapter("Chapter 2", 89))
    #b1.addchapter(Chapter("Chapter 3", 124))
  
    #print(b1.title)
    #print(b1.author)
    print(t1.getFishingTripInformation())

if __name__ == "__main__":
  main()

#date1 = datetime.datetime(2020, 10, 31)
#startTime1 = "10:00"
#endTime1 = "14:00"
#lake1 = "Hillsdale"
#waterTemp1 = 67
#fishCaught1 = 11
#airTemp1 = 56
#windSpeed1 = 11
#windDirection1 = "West"
#
#print("**DEBUG** The trip information for trip: \n" + 
#    "Date: " + str(date1) + "\n" + 
#    "Start Time: " + str(startTime1) + "\n" + 
#    "End time: " + str(endTime1) + "\n" + 
#    "on lake: " + str(lake1) + "\n" + 
#    "with water temperature:" + str(waterTemp1) + "\n" + 
#    "caught " + str(fishCaught1) + " fish  caught " + "\n" + 
#    "air temperature of: " + str(airTemp1) + " degrees farenheight" + "\n" + 
#    "wind blowing at " + str(windSpeed1) + " mph" + "\n" + 
#    "out of the " + str(windDirection1)
#    )
#
##build the first trip
#t1 = fishingTrip("10/31/2020", startTime1, endTime1, lake1, waterTemp1, fishCaught1, airTemp1, windSpeed1, windDirection1)
#print("**DEBUG** The date of the fishing trip is:" + str(t1.date))
##b1.addchapter(Chapter("Chapter 1", 104))
##b1.addchapter(Chapter("Chapter 2", 89))
##b1.addchapter(Chapter("Chapter 3", 124))
#
##print(b1.title)
##print(b1.author)
#print(t1.getFishingTripInformation())