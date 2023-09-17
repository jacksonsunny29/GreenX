from prompting import TextAnalyser
import numpy as np
from hotelRanker import hotelsID, hotelsMatrix
from cal_latlongdist import haversine

class HotelFinder(object):

    def __init__(self, inText) -> None:
        self.topicWeights = np.array(list(TextAnalyser(inText=inText).getSents().values()))
        # could need transpositions
        self.scores = np.dot(hotelsMatrix, self.topicWeights) + np.array([h[2] for h in hotelsID])

    def getNBestScorers(self, n):
        indeces = np.argsort(-self.scores)[:n]
        lats = [hotelsID[i][1]['latitude'] for i in indeces]
        longs = [hotelsID[i][1]['longitude'] for i in indeces]
        # print(lats,longs)
        dists=[]
        for i,j in zip(lats,longs):
            dist=haversine(float(i),float(j))
            print(dist) 
            dists.append(dist)
        print(dists)
        return [(*hotelsID[i], dists[i]) for i in indeces]
