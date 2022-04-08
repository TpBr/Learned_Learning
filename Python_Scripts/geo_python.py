#Importing important modules
import tkinter
import math
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json

# To use, see the last function in this file, startGUI().

# Given a string representing a location, return 2-element 
# [latitude, longitude] list for that location 
#
def geocodeAddress(addressString):
   global url
   urlbase = "http://maps.googleapis.com/maps/api/geocode/json?address="
   url = urlbase + quote_plus(addressString)
   
   stringResultFromGoogle = urlopen(url).read().decode('utf8')
   jsonResult = json.loads(stringResultFromGoogle)
   if (jsonResult['status'] != "OK"):
      print("Status returned from Google geocoder *not* OK: {}".format(jsonResult['status']))
      return
   loc = jsonResult['results'][0]['geometry']['location']
   return (float(loc['lat']),float(loc['lng']))


# Contruct a Google Static Maps API URL that specifies a map that is:
# - width-by-height in size (in pixels)
# - is centered at latitude lat and longitude long
# - is "zoomed" to the give Google Maps zoom level
#

# See https://developers.google.com/maps/documentation/static-maps/
#    ALSO:
# 1) DISPLAYS A PIN ON THE MAP
# 2) SETS MAP TYPE
#
def getMapUrl(width, height, lat, lng, zoom, maptype):
   urlbase = "http://maps.google.com/maps/api/staticmap?"
   args = "center={},{}&zoom={}&size={}x{}&format=gif&maptype={}&markers={},{}".format(lat,lng,zoom,width,height,maptype,lat,lng)
   return  urlbase+args

# This program retrieves a map image via Google Static Maps API:
# - centered at the location specified by global variable mapLocation
# - zoomed according to global variable zoomLevel (Google's zoom levels range from 0 to 21)
# - width and height equal to global variable mapSize
# - mapType as specified
# Stores the returned image in file name specified by global variable mapFileName
#
def retrieveMap():
   lat, lng = geocodeAddress(mapLocation)
   url = getMapUrl(mapSize, mapSize, lat, lng, zoomLevel, mapType)
   urlretrieve(url, mapFileName)
   return mapFileName
   
   
#raiseZoomAndShowMap and lowerZoomAndShowMap functions serve as commands for the zoom in an zoom out buttons.  
#The code is almost word for word the instructions given in the homework.  
def raiseZoomAndShowMap():
    global zoomLevel
    zoomLevel += 1  
    showMap()
    
    
def lowerZoomAndShowMap():
    global zoomLevel
    zoomLevel -= 1
    showMap()
    
    
#This function serves as the command for the change view button which, when clicked, will cycle through and set maptype to different type.
def changeViewAndShowMap():
    global mapType
    if mapType == "roadmap":
        mapType = "terrain"
        showMap()
    elif mapType == "terrain":
        mapType = "satellite"
        showMap()
    elif mapType == "satellite":
        mapType = "hybrid"
        showMap()
    else:
        mapType = "roadmap"
        showMap()
        
        
########## 
# very basic GUI code

# Global variables used by GUI and map code
#

rootWindow = None
mapLabel = None

defaultLocation = "Mauna Kea, Hawaii"
mapLocation = defaultLocation
mapFileName = 'googlemap.gif'
mapSize = 400
zoomLevel = 9
mapType = "roadmap"

def readEntryAndShowMap():
   global mapLocation
   
   #get method retrieves the text from the entry widget to use as the location if somebody inputted an address, else the program uses default location.
   if textEntry.get() != "":
       mapLocation = textEntry.get() 
       showMap()
   else:
       showMap()
       
       
def showMap():
   retrieveMap()    
   mapImage = tkinter.PhotoImage(file=mapFileName)
   mapLabel.configure(image=mapImage)
   # next line necessary to "prevent (image) from being garbage collected" - http://effbot.org/tkinterbook/label.htm
   mapLabel.mapImage = mapImage 
   
  
def initializeGUIetc():
   global rootWindow
   global mapLabel
   global textEntry

   rootWindow = tkinter.Tk()
   rootWindow.title("HW9 Q2")

   mainFrame = tkinter.Frame(rootWindow) 
   mainFrame.pack()

   

   #We use a tkinter Label to display the map   
   mapLabel = tkinter.Label(mainFrame, bd=2, relief=tkinter.FLAT)
   mapLabel.pack()
   
   #Some of the labels and buttons are padded to make the spacing appropriate for the app.
   entryLabel = tkinter.Label(mainFrame, text = "Enter the location:")
   entryLabel.pack(side = tkinter.LEFT, padx = 23)
   
   textEntry = tkinter.Entry(mainFrame, width = 17)
   textEntry.pack(side = tkinter.LEFT, padx = 0)
   textEntry.focus_set()
   
   #readEntryAndShowMapButton allows the user to look at different locations
   readEntryAndShowMapButton = tkinter.Button(mainFrame, text="Show me the map!", command=readEntryAndShowMap)
   readEntryAndShowMapButton.pack(side = tkinter.RIGHT)
   
   #zoomInButton and zoomOutButton allow the user to adjust the distance of view the specified location
   zoomInButton = tkinter.Button(mainFrame, height = 1, width = 1, text="+", command=raiseZoomAndShowMap)
   zoomInButton.pack(side = tkinter.LEFT, padx = 0)
   zoomOutButton = tkinter.Button(mainFrame, height = 1, width = 1, text="-", command=lowerZoomAndShowMap)
   zoomOutButton.pack(side = tkinter.LEFT)
   
   #This frame places the view change button on the absolute bottom of the main frame.
   viewFrame = tkinter.Frame(rootWindow)
   viewFrame.pack(side = tkinter.BOTTOM)
   
   #View Button, when clicked, cycles through the maptypes one click at a time.
   mapTypeButton = tkinter.Button(viewFrame, text="Change View", command=changeViewAndShowMap)
   mapTypeButton.pack()
   
   

def startGUI():
    initializeGUIetc()
    showMap()
    rootWindow.mainloop()
