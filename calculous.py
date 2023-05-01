from typing import Optional
from attenuations import atmospheric
from attenuations.ground import AGround
from attenuations.divergence import divergence
from attenuations.barrier import BarrierAttenuation
from utils.feature_extractions import FeatureExtractions
from objects import Source, Receiver, Barrier
from params import Params
import numpy as np

class SoundPressureLevel:
    def __init__(self,source:Source, 
                     receiver:Receiver,
                     barrier:Optional[Barrier]=None) -> None:
        self.source = source
        self.receiver = receiver
        self.barrier = barrier
        self.features = FeatureExtractions(source, receiver, barrier)

    @property
    def get_noise_level(self):
        attenuations = self.get_attenuations()
        spl = self.source.lw+Params.D_C-attenuations
        def validate_value(value:float):
            return value if value>0 else 0
        return np.array([validate_value(x) for x in spl])
    
    def get_attenuations(self):
        if self.barrier:
            return (self.atm_attenuation + 
                    self.ground_attenuation + 
                    self.divergence_attenuation + 
                    self.barrier_attenuation)
        return self.atm_attenuation + self.ground_attenuation + self.divergence_attenuation

    @property
    def atm_attenuation(self):
        return atmospheric.atm_attenuation(self.features.d)

    @property
    def ground_attenuation(self):
        a_ground = AGround(Params, self.source, self.receiver)
        attenuation_ground = a_ground.get_attenuation
        return attenuation_ground

    @property
    def divergence_attenuation (self):
        return divergence(self.features.d)
    
    @property
    def barrier_attenuation(self):
        a_barrier = BarrierAttenuation(self.source, self.receiver, self.barrier)
        return a_barrier.dz