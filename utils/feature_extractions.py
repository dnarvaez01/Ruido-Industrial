from typing import Optional
from objects import Source, Receiver, Barrier
from typing import Tuple
import numpy as np

def distance(position1:Tuple[float], position2:Tuple[float]):
    position1 = np.array(position1)
    position2 = np.array(position2)
    return np.sqrt(((position1-position2)**2).sum())

class FeatureExtractions:
    def __init__(self, source:Source, receiver:Receiver, barrier:Optional[Barrier]=None) -> None:
        self.source = source
        self.receiver = receiver
        self.barrier = barrier
        self.__get_features__()

    def __get_features__(self):
        self.d = distance(self.source.position, self.receiver.position)
        self.hs = self.source.height
        self.hr = self.receiver.height
        if self.barrier:
            self.__get_barrier_features__()

    def __get_barrier_features__(self):
        self.dss = np.sqrt(self.barrier.distance**2 + 
                           (self.barrier.height-self.source.height)**2)
        self.dsr = np.sqrt((self.d-self.barrier.distance-self.barrier.e)**2 + 
                           (self.barrier.height-self.receiver.height)**2)
        self.a = np.abs(self.receiver.height - self.source.height)