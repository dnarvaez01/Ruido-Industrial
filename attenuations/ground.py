import numpy as np
from objects import Source, Receiver
from utils.feature_extractions import distance
from params import Params

class GroundAttenuation:
    def __init__(self, h:float, g:float, dp:float) -> None:
        self.h = h
        self.g = g
        self.dp = dp
        self.__calculate_functions__()

    def __calculate_functions__(self):
        self.a = 1.5 + (3*np.exp(-0.12*(self.h-5)**2)*(1-np.exp(-self.dp/50))+
                        5.7*np.exp(-0.09*self.h**2)*(1-np.exp(-2.8*10**(-6*self.dp**2))))
        self.b = 1.5 + 8.6*np.exp(-0.09*self.h**2)*(1-np.exp(-self.dp/50))
        self.c = 1.5 + 14*np.exp(-0.46*self.h**2)*(1-np.exp(-self.dp/50))
        self.d = 1.5 + 5*np.exp(-0.9*self.h**2)*(1-np.exp(-self.dp/50))

    def get_by_frequency(self):
        a_63 = 1.5
        a_125 = -1.5+self.g*self.a
        a_250 = -1.5+self.g*self.b
        a_500 = -1.5+self.g*self.c
        a_1000 = -1.5+self.g*self.d
        a_2000 = -1.5*(1-self.g)
        a_4000 = -1.5*(1-self.g)
        a_8000 = -1.5*(1-self.g)
        aux = np.array([a_63, a_125, a_250, a_500, a_1000, a_2000, a_4000, a_8000])
        return aux
    
class AGround:
    def __init__(self, params:Params, source:Source, receiver:Receiver) -> None:
        self.g_source = params.G_SOURCE
        self.g_middle = params.G_MIDDLE
        self.g_receiver = params.G_RECEIVER
        self.source = source
        self.receiver = receiver 
        
    @property
    def source_region(self):
        return 30*self.source.height
    
    @property
    def receiver_region(self):
        return 30*self.receiver.height
    
    @property
    def dp(self):
        return distance(self.source.position[:2],self.receiver.position[:2])
    
    @property
    def middle_region(self):
        result = self.dp-self.source_region-self.receiver_region
        return result if result>0 else None
    
    def a_s(self):
        source_attenuation = GroundAttenuation(self.source.height, self.g_source, self.dp)
        return source_attenuation.get_by_frequency()
    def a_r(self):
        receiver_attenuation = GroundAttenuation(self.receiver.height, self.g_receiver, self.dp)
        return receiver_attenuation.get_by_frequency()
    def a_m(self):
        q = 1 - 30*(self.source.height+self.receiver.height)/self.dp if self.middle_region else 0
        return np.array([-3*q**2,
                         -3*q*1-self.g_middle,
                         -3*q*1-self.g_middle,
                         -3*q*1-self.g_middle,
                         -3*q*1-self.g_middle,
                         -3*q*1-self.g_middle,
                         -3*q*1-self.g_middle,
                         -3*q*1-self.g_middle])
    
    @property
    def get_attenuation(self):
        a_s = self.a_s()
        a_r = self.a_r()
        a_m = self.a_m()
        return a_s + a_r + a_m