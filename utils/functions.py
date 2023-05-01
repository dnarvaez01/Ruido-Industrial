from typing import Iterable, Literal
import numpy as np

def leq(values:Iterable[float], weighting) -> float:
    a_weighting_values = np.array(values)+np.array(weighting)
    return 10*np.log10((10**(0.1*(a_weighting_values))).sum())

def weighting_values(values:Iterable[float], weighting):
    return np.array(values)+np.array(weighting)