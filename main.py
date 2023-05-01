from utils.constants import OCT_A_WEIGHTING, FREQ_OCT
from objects import Source, Receiver, Barrier
from params import Params
from utils.functions import leq
from calculous import SoundPressureLevel
import numpy as np
import pandas as pd

def get_spl_by_receiver(activate_barrier: bool):
    source = Params.SOURCE_POSITIONS['FC']
    lw = np.array(Params.LW_FUENTES['FC'])
    spl_table = pd.DataFrame(columns=(*FREQ_OCT, 'LAeq', 'Distance'))
    atm_table = pd.DataFrame(columns=FREQ_OCT)
    div_table = pd.DataFrame(columns=FREQ_OCT)
    ground_table = pd.DataFrame(columns=FREQ_OCT)
    barrier_table = pd.DataFrame(columns=FREQ_OCT)
    for receiver, position in Params.RECEIVER_POSITIONS.items():
        if activate_barrier:
            spl_class = SoundPressureLevel(Source(source, lw), 
                                    Receiver(position), 
                                    Barrier(Params.DISTANCE_TO_BARRIER,
                                            Params.BARRIER_HEIGHT,
                                            Params.BARRIER_THICKNESS*.1))
        else:
            spl_class = SoundPressureLevel(Source(source, lw), 
                                    Receiver(position))
            
        spl = spl_class.get_noise_level
        laeq = round(leq(spl, OCT_A_WEIGHTING))
        spl_table.loc[receiver] = (*spl, laeq, round(spl_class.features.d))    
        atm_table.loc[receiver] = spl_class.atm_attenuation
        div_table.loc[receiver] = spl_class.divergence_attenuation
        ground_table.loc[receiver] = spl_class.ground_attenuation
        if activate_barrier:
            barrier_table.loc[receiver] = spl_class.barrier_attenuation

    tables = [atm_table, div_table, ground_table, barrier_table]
    attenuation_tables = pd.concat(tables, keys=['atm_table', 
                                         'div_table', 
                                         'ground_table', 
                                         'barrier_table'])
    
    idx = attenuation_tables.index
    idx.set_names(['Attenuation', 'Receiver'], inplace=True)
    attenuation_tables.set_index(idx)
    attenuation_tables_by_receiver = attenuation_tables.reorder_levels(['Receiver', 'Attenuation']).groupby(level=[0,1]).sum()
    return spl_table, attenuation_tables

def main():
    spl, attenuations = get_spl_by_receiver(activate_barrier=False)
    spl_barrier, attenuations_barrier = get_spl_by_receiver(activate_barrier=True)
    spl_tables = [spl, spl_barrier]
    spl_tables = pd.concat(spl_tables, keys=['SPL WITHOUT BARRIER', 
                                             'SPL WITH BARRIER'])
    

    with pd.ExcelWriter(Params.RESULTS_DIR) as writer:
        spl_tables.to_excel(writer,sheet_name='SPL BY RECEIVER')
        attenuations_barrier.to_excel(writer,sheet_name='ATTENUATIONS BY RECEIVER')

if __name__=='__main__':
    main()
