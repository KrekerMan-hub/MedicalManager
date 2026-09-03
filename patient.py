#========================
# Хранение class Patient
#========================

from enum import Enum
from datetime import datetime

class Department(Enum):
    THERAPY = "Терапия"
    SURGERY = "Хирургия"
    ICU = "Реанимация"

class PatientStatus(Enum):
    ADMITTED = "Госпитализирован"
    DISCHARGED = "Выписан"
    TRANSFERRED = "Переведен"


class Patient:

    def __init__(self, name, age, diagnosis, department, status, admission_time=None):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.department = department
        self.status = status
        if admission_time is None:
            self.admission_time = datetime.now()
        else:
            self.admission_time = admission_time


    def __str__(self):
        admission = self.admission_time.strftime("%d.%m.%Y %H:%M")

        return(f"{self.name}, {self.age}\nДиагноз: {self.diagnosis}\n"
               f"Поступил: {admission}\n"
               f"Отделение: {self.department.value}\n"
               f"Статус: {self.status.value}")

    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "diagnosis": self.diagnosis,
            "department": self.department.value,
            "status": self.status.value,
            "admission": self.admission_time.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["diagnosis"],
            Department(data["department"]),
            PatientStatus(data["status"]),
            datetime.fromisoformat(data["admission"]),
        )