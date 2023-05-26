import numpy as np
from dataclasses import dataclass

FREQ_OCT = (63,125,250,500,1000,2000,4000,8000)
OCT_A_WEIGHTING = (-26.2, -16.1, -8.6, -3.2, 0, 1.2, 1, -1.1)
OCT_B_WEIGHTING = (-26.2, -16.1, -8.6, -3.2, 0, 1.2, 1, -1.1)
OCT_C_WEIGHTING = (-26.2, -16.1, -8.6, -3.2, 0, 1.2, 1, -1.1)

FREQ_TER = (50,63,80,100,125,160,200,250,315,400,
            500,630,800,1000,1250,1600,2000,2500,
            3150,4000,5000,6300,8000,10000)
TER_A_WEIGHTING = (-30.2, -26.2, -22.5, -19.1, -16.1,
                   -13.4, -10.9, -8.6, -6.6, -4.8,
                   -3.2, -1.9, -0.8, 0, 0.6,
                   1, 1.2, 1.3, 1.2, 1,
                   0.5, -0.1, -1.1, -2.5)
C = 343.3
_LAMBDA = C/np.array(FREQ_OCT)
_LAMBDA_TER = C/np.array(FREQ_TER)

@dataclass
class Weightings:
    a = OCT_A_WEIGHTING
    b = OCT_B_WEIGHTING
    c = OCT_C_WEIGHTING