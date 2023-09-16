from prompting import TextAnalyser
import numpy as np

class HotelFinder(object):
    
    hotelMatrix, hotelIds = ([], [])

    def __init__(self, inText) -> None:
        self.topicWeights = np.array(TextAnalyser(inText=inText).getSents().values())
        # could need transpoisitions
        self.scores = np.matmul(HotelFinder.hotelMatrix, self.topicWeights)

    def getNBestScorers(self, n):
        indeces = np.argsort(-self.scores)[:n]
        return [HotelFinder.hotelIds[i] for i in indeces]