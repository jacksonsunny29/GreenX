import os
from dotenv import load_dotenv, find_dotenv 
# from carboninterface import CarbonInterface
from haversine import haversine
load_dotenv(find_dotenv('config.env'))

def calc_CarbonFlight(source,dest):
    API_FLIGHT_KEY = os.getenv("API_FLIGHT_KEY")
    # ci = CarbonInterface(api_key=API_FLIGHT_KEY, units="kg")
    # x = ci.estimate_flight(source, dest)
    distance = haversine(source,dest)
    x = distance*40/1000
    return int(x)
    # x=x/person
    return int(x)

def calc_CarbonTrain(source,dest):
    distance = haversine(source,dest)
    x = distance*9/1000
    return int(x)
