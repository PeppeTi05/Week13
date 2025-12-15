from dataclasses import dataclass
from arts_mia.model.object import Object

@dataclass
class Connessione:
    o1 : Object # Approccio ORM -- inserisco nella classe connessione degli Oggetti
    o2 : Object
    peso : int