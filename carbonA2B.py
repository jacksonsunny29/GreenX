import os
from dotenv import load_dotenv, find_dotenv 
from carboninterface import CarbonInterface
from catlatlongdist import haversine
load_dotenv(find_dotenv('config.env'))

def calc_CarbonFlight(source,dest,person):
    API_FLIGHT_KEY = os.getenv("API_FLIGHT_KEY")
    ci = CarbonInterface(api_key=API_FLIGHT_KEY, units="kg",passengers=2)
    x = ci.estimate_flight(source, dest)
    x=x/person
    return int(x)

def calc_CarbonTrain(source,dest):
    distance = haversine(source,dest)
    x = distance*9/1000
    return int(x)
