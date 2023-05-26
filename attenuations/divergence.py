import numpy as np

def divergence(distance: float, d0:int=1) -> float:
    return 20*np.log10(distance/d0)+11
