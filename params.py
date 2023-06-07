from dataclasses import dataclass
from utils.abs_coef import Material, ABSORPTION


@dataclass
class Params_:
    RESULTS_DIR = 'F:\Dani\spl_values.xlsx'
    DISTANCE_TO_BARRIER = 30 
    BARRIER_HEIGHT = 2.4 #h in m
    BARRIER_THICKNESS = 0.15 #e in cm
    SOURCE_POSITIONS = {'F1':(289782,6363955,1.2),
                        'F2':(289788,6363955,1.2),
                        'F3':(289782,6363979,1.2),
                        'FC':(289782,6363967,1.2)}
    
    BARRIER_POSITIONS = { 'B1':(289782+DISTANCE_TO_BARRIER, BARRIER_HEIGHT), # +x
                          'B2':(289782-DISTANCE_TO_BARRIER, BARRIER_HEIGHT), #-x
                          'B3':(6363967+DISTANCE_TO_BARRIER, BARRIER_HEIGHT), #+Y
                          'B4':(6363967-DISTANCE_TO_BARRIER, BARRIER_HEIGHT)} #-Y

    RECEIVER_POSITIONS = {'R1':(289827,6363825,1.5),
                          'R2':(289398,6363754,1.5),
                          'R3':(290587,6364355,1.5),
                          'R4':(290736,6363776,1.5),
                          'R5':(289782,6364017,1.5)}

    LW_FUENTES = {'F1':(65.1,78.3,87.6,96.4,99.8,99.1,94.3,84.4),
                  'F2':(65.1,78.3,87.6,96.4,99.8,99.1,94.3,84.4),
                  'F3':(53.1,66.2,75.7,84.1,87.3,87.5,82.3,72.2),
                  'FC':(68.25,81.44,90.75,99.54,102.93,102.26,97.45,87.54)}
    D_C = 0
    G_SOURCE = 0
    G_MIDDLE = 1
    G_RECEIVER = 0.5


@dataclass
class Params:
    RESULTS_DIR = 'F:\Dani\spl_values.xlsx'
    DISTANCE_TO_BARRIER = 30 
    BARRIER_HEIGHT = 2.4 #h in m
    BARRIER_THICKNESS = 0.15 #e in cm
    SOURCE_POSITIONS = {'F1':(289782,6363955,1.2),
                        'F2':(289788,6363955,1.2),
                        'F3':(289782,6363979,1.2),
                        'FC':(289782,6363967,1.2)}
    
    BARRIER_POSITIONS = { 'B1':(289782+DISTANCE_TO_BARRIER, BARRIER_HEIGHT), # +x
                          'B2':(289782-DISTANCE_TO_BARRIER, BARRIER_HEIGHT), #-x
                          'B3':(6363967+DISTANCE_TO_BARRIER, BARRIER_HEIGHT), #+Y
                          'B4':(6363967-DISTANCE_TO_BARRIER, BARRIER_HEIGHT)} #-Y

    RECEIVER_POSITIONS = {'R1':(289827,6363825,1.5),
                          'R2':(289398,6363754,1.5),
                          'R3':(290587,6364355,1.5),
                          'R4':(290736,6363776,1.5),
                          'R5':(289782,6364017,1.5)}

    LW_FUENTES = {'F1':(65.1,78.3,87.6,96.4,99.8,99.1,94.3,84.4),
                  'F2':(65.1,78.3,87.6,96.4,99.8,99.1,94.3,84.4),
                  'F3':(53.1,66.2,75.7,84.1,87.3,87.5,82.3,72.2),
                  'FC':(68.25,81.44,90.75,99.54,102.93,102.26,97.45,87.54)}
    D_C = 0
    G_SOURCE = 0
    G_MIDDLE = 1
    G_RECEIVER = 0.5

@dataclass
class InteriorParams:
    RESULTS_DIR = 'F:\Dani\spl_values.xlsx'

    SOURCE_POSITIONS = {'F1':(289782,6363955,1.2),
                        'F2':(289788,6363955,1.2),
                        'F3':(289782,6363979,1.2),
                        'FC':(289782,6363967,1.2)}

    LW_FUENTES = {'F1':(65.1,78.3,87.6,96.4,99.8,99.1,94.3,84.4),
                  'F2':(65.1,78.3,87.6,96.4,99.8,99.1,94.3,84.4),
                  'F3':(53.1,66.2,75.7,84.1,87.3,87.5,82.3,72.2),
                  'FC':(68.25,81.44,90.75,99.54,102.93,102.26,97.45,87.54)}

    MATERIALS = {'Wall_N' : Material(210, ABSORPTION.wall),
                'Wall_S' : Material(210, ABSORPTION.wall),
                'Wall_E' : Material(140, ABSORPTION.wall),
                'Wall_W' : Material(140, ABSORPTION.wall),
                'Ceiling': Material(600, ABSORPTION.wall),
                'Floor'  : Material(600, ABSORPTION.floor)}
    
    SURFACE = 1900
