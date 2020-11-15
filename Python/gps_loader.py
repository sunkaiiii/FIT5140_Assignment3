from gps import *
from json import JSONEncoder
import time

running = True
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

# sudo gpsd /dev/ttyACM0 -F /var/run/gpsd.sock
# sudo cgps -s

# Extract GPS information from the GPS module.
# References on https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi

class GPSInformationExtractor:
    class GPSInformationResult():
        def __init__(self):
            self.latitude = 0
            self.longitude = 0
    def get_current_position(self):
        result = self.GPSInformationResult()
        while(result.latitude == 0):
            nx = gpsd.next()
            if nx['class'] == 'TPV':
                print(nx)
                latitude = getattr(nx,'lat', "Unknown")
                longitude = getattr(nx,'lon', "Unknown")
                result.latitude = latitude
                result.longitude = longitude
                print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
                return result
        return result

def getPositionData():
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        print(nx)
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))

if __name__=="__main__":

    GPSInformationExtractor().get_current_position()
    # try:
    #     print("Application started!")
    #     while running:
    #         getPositionData()
    #         time.sleep(1.0)

    # except (KeyboardInterrupt):
    #     running = False
    #     print("Applications closed!")