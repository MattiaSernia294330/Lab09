from dataclasses import dataclass
@dataclass
class Aereoporto:
    ID: str
    AIRPORT: str

    def __hash__(self):
        return hash(self.ID)

    def __str__(self):
        return f"{self.ID} - {self.AIRPORT}"
