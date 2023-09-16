from prompting import TextAnalyser
import numpy as np
from hotelRanker import hotelsID, hotelsMatrix


class HotelFinder(object):

    def __init__(self, inText) -> None:
        self.topicWeights = np.array(list(TextAnalyser(inText=inText).getSents().values()))
        # could need transpositions
        self.scores = np.dot(hotelsMatrix, self.topicWeights) + np.array([h[2] for h in hotelsID])

    def getNBestScorers(self, n):
        indeces = np.argsort(-self.scores)[:n]
        return [hotelsID[i] for i in indeces]
