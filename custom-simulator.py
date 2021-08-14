import os
import time
from time import gmtime, strftime
import datetime
import dateutil.parser
from datetime import timedelta

from time import sleep
from clint.textui import colored
from yamcs.client import YamcsClient
import math

from random import seed
from random import random
seed(1)

yamcs_address = "localhost:8090"
plant_name = "myproject"
plant_str = "/" + plant_name + "/"
client = YamcsClient(yamcs_address)
processor = client.get_processor(instance=plant_name, processor='realtime')

def initializeParameters():
    try:
        print(colored.cyan("\n\t\t  * * Attempting to set parameters * *\n"))
        random_latitude = 0 + (random() * (90 - 0))
        print('Latitude: ' + str(random_latitude))
        random_longitude = 0 + (random() * (180 - 0))
        print('Longitude: ' + str(random_longitude))
        processor.set_parameter_value(plant_str + "Rover_Latitude", round(random_latitude, 4))
        processor.set_parameter_value(plant_str + "Rover_Longitude", round(random_longitude, 4))
        print(colored.cyan("\n\t\t  * * Latitude and Logitude have been set. * *\n"))
    except:
        print(colored.magenta("\n\t\tConnection Error:  Initialization has failed.\n\n\n"))


def endFn(): 
    while(True):
        sleep(1.5)
        if(True):
            connected = True
            try:
                processor.get_parameter_value(plant_str + "Rover_Latitude")
                processor.get_parameter_value(plant_str + "Rover_Longitude")
            except:
                connected = False
            if(connected == False):
                print(colored.red("\t\tDISCONNECTED" + "\n"))
                global initialized
                initialized = False
                break
            else:
                print("\n\n") 
                print("DONE") 
                print("\n\n") 


def mainLoop(): 
    while(True):
        initializeParameters()
        sleep(3)

if __name__ == "__main__":
    print('starting!')
    mainLoop()