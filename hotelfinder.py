from prompting import TextAnalyser
import numpy as np
from hotelRanker import hotelsID, hotelsMatrix
import carbonA2B
from haversine import haversine

ZURICH_COORDS = (47.4, 8.5)


class HotelFinder(object):

    def __init__(self, inText) -> None:
        self.topicWeights = np.array(list(TextAnalyser(inText=inText).getSents().values()))
        # could need transpositions
        self.scores = np.dot(hotelsMatrix, self.topicWeights) + np.array([h[2] for h in hotelsID])

    def getNBestScorers(self, n):
        indeces = np.argsort(-self.scores)[:n]
        dists={}
        emits={}
        for i in indeces:
            lat = hotelsID[i][1]['latitude']
            long = hotelsID[i][1]['longitude']
            dist=haversine(ZURICH_COORDS, (lat,long))
            dists[i] = (dist)
            emits[i] = (
                {
                    "air": carbonA2B.calc_CarbonFlight(ZURICH_COORDS, (lat,long)),
                    "rail": carbonA2B.calc_CarbonTrain(ZURICH_COORDS, (lat,long))
                }
            )            
        return [(("https://www.hotelplan.ch/" + hotelsID[i][0]), int(dists[i]), emits[i], hotelsID[i][3]) for i in indeces]
