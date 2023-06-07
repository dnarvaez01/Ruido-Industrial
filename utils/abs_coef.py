from dataclasses import dataclass
import numpy as np

@dataclass
class ABSORPTION:
    wall=np.array([0.23,0.057,0.014,0.003,0,0])
    floor=np.array([0.01,0.01,0.02,0.02,0.02,0.03])
    anechoic=np.array([0.99,0.99,0.99,0.99,0.99,0.99])

@dataclass
class Material:
    surface:float
    absorption:ABSORPTION

    @property
    def area_abs_eq(self):
        return self.absorption*self.surface
