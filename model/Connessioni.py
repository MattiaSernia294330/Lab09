from dataclasses import dataclass
@dataclass
class Connessione():
    ID:int
    ORIGIN_AIRPORT_ID:int
    DESTINATION_AIRPORT_ID:int
    DISTANCE:float



def __hash__(self):
    return hash(self._ID)