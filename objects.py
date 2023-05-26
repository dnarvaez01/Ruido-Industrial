from typing import Tuple, Optional

class Source:
    def __init__(self, position:Tuple[float, float, float], lw:float) -> None:
        self.position = position
        self.lw = lw
        self.height = position[-1]

    @property
    def get_pos(self):
        return self.position[0], self.position[2]
    
class Receiver:
    def __init__(self, position:Tuple[float, float, float]) -> None:
        self.position = position
        self.height = position[-1]

    @property
    def get_pos(self):
        return self.position[0], self.position[2]
    
class Barrier:
    def __init__(self, distance:float, height:float, e:Optional[float]=0) -> None:
        self.distance = distance #Source-Barrier
        self.height = height
        self.e = e #Thickness barrier
    
    @property
    def get_pos(self):
        return self.distance, self.height
    
    @property
    def get_delta_pos(self):
        return self.distance + self.e, self.height
    