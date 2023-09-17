import json
import numpy as np

hotelsVectors = []
hotelsID = []

with open('fr.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for continent in data['geo']:
    for countriesPage in continent['countries']['countriesPage']:
        for destinationPage in countriesPage['destinations']['destinationsPage']:
            for resortsPage in destinationPage['resorts']['resortsPage']:
                if resortsPage['products']['productsPage'] is None:
                    continue
                for hotels in resortsPage['products']['productsPage']:
                    beautyAndWellness = hotels['flags']['beautyAndWellness']['achieved']
                    modernDesign = hotels['flags']['typeFlags']['modernDesign']
                    waterSports = hotels['flags']['waterSport']['achieved']
                    sport = hotels['flags']['sport']['achieved']
                    beachFront = hotels['flags']['location']['beachFront']
                    cityCenter = hotels['flags']['location']['cityCenter']
                    rural = hotels['flags']['location']['ruralArea']
                    directlyAtLake = hotels['flags']['location']['directlyAtLake']
                    family = hotels['flags']['family']['achieved']
                    luxury = hotels['flags']['typeFlags']['luxury']
                    wheelchairAccess = hotels['flags']['typeFlags']['wheelchairAccess']
                    parking = hotels['flags']['typeFlags']['parking']
                    appartement = hotels['flags']['typeFlags']['apartment']
                    entertainment = hotels['flags']['entertainment']['achieved']
                    bar = hotels['flags']['foodAndBeverage']['bar']
                    ski = hotels['flags']['ski']

                    sustainabilityHeuristic = 0
                    if waterSports:
                        sustainabilityHeuristic -= 0.1
                    if rural:
                        sustainabilityHeuristic-= 0.1

                    hotels_vector = (np.array([beautyAndWellness, modernDesign, waterSports, sport, beachFront,
                                              cityCenter, rural, directlyAtLake, family, luxury, wheelchairAccess,
                                              parking, appartement, entertainment, bar, ski]).astype(int) * 2 - 1) * 10

                    hotelsVectors.append(hotels_vector)
                    hotelsID.append((hotels['publicId'], hotels["coordinates"], sustainabilityHeuristic))

hotelsMatrix = np.array(hotelsVectors)