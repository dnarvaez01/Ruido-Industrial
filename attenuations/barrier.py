from objects import Source, Receiver, Barrier
from utils.feature_extractions import FeatureExtractions
from utils.constants import _LAMBDA
import numpy as np


class BarrierAttenuation(FeatureExtractions):
    def __init__(self, source: Source, receiver: Receiver, barrier: Barrier) -> None:
        super().__init__(source, receiver, barrier)
        self.receiver = receiver
        self.source = source
        self.barrier = barrier
        self.c2 = 20
        if barrier:
            self.e = barrier.e
        
    @property
    def z(self):
        return np.sqrt((self.dss+self.dsr+self.e)**2+(self.a)**2)-self.d
    
    @property
    def kmet(self):
        return np.exp(-(1/2000)*np.sqrt(
            self.dss*self.dsr*self.d/(2*self.z))) if self.z>0 else 1
    @property
    def _c3_(self): 
        return ((1+(5*_LAMBDA/self.e)**2)/(1/3+(5*_LAMBDA/self.e)**2)) if self.e!=0 else 1
    
    @property
    def dz(self):
        return 10*np.log10(3+(self.c2/_LAMBDA)*self._c3_*self.z*self.kmet)
