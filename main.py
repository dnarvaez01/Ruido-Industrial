from utils.constants import OCT_A_WEIGHTING, FREQ_OCT
from objects import Source, Receiver, Barrier
from params import Params
from utils.functions import leq, weighting_values
from calculous import SoundPressureLevel
import numpy as np
import pandas as pd
import time

def walk_sources_receivers():
    source = Params.SOURCE_POSITIONS['FC']
    lw = np.array(Params.LW_FUENTES['FC'])
    spl_table = pd.DataFrame(columns=(*FREQ_OCT, 'LAeq', 'Distance'))
    atm_table = pd.DataFrame(columns=FREQ_OCT)
    div_table = pd.DataFrame(columns=FREQ_OCT)
    ground_table = pd.DataFrame(columns=FREQ_OCT)
    barrier_table = pd.DataFrame(columns=FREQ_OCT)
    for receiver, position in Params.RECEIVER_POSITIONS.items():
        spl_class = SoundPressureLevel(Source(source, lw), 
                                Receiver(position), 
                                Barrier(Params.DISTANCE_TO_BARRIER,
                                        Params.BARRIER_HEIGHT))
        spl = spl_class.get_noise_level
        laeq = round(leq(spl, OCT_A_WEIGHTING))
        spl_table.loc[receiver] = (*spl, laeq, round(spl_class.features.d))    
        atm_table.loc[receiver] = spl_class.atm_attenuation
        div_table.loc[receiver] = spl_class.divergence_attenuation
        ground_table.loc[receiver] = spl_class.ground_attenuation
        barrier_table.loc[receiver] = spl_class.barrier_attenuation

    print('SPL TABLE:')
    print(spl_table)    
    print('atm_table')
    print(atm_table)
    print('div_table')
    print(div_table)
    print('ground_table')
    print(ground_table)
    print('barrier_table')
    print(barrier_table)

def main():
    tic = time.time()
    walk_sources_receivers()
    toc = time.time()
    print(f'Process time = {(toc-tic)*1000} ms.')

if __name__=='__main__':
    main()
