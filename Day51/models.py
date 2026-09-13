#=======================
# dataclass
#=======================

from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    name: str
    age: int | None = None
    diagnosis: str | None = None