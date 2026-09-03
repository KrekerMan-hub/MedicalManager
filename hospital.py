#========================
# Хранения class Hospital
#========================

import json
from patient import Patient

class Hospital:

    def __init__(self, filename):
        self.patients = []
        self.filename = filename

    def save_patients(self):
        data = []
        for patient in self.patients:
            data.append(patient.to_dict())
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_patients(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.patients = []
                for patient_data in data:
                    patient = Patient.from_dict(patient_data)

                    self.patients.append(patient)  

        except FileNotFoundError:
            self.patients = []
            print("Файл не найден")
        except json.JSONDecodeError:
            print("Содержание файла повреждено")

    def add_patient(self, patient):
        for existing_patient in self.patients:
            if existing_patient.name == patient.name:
                print("Такой пациент уже существует.")
                return
            
        self.patients.append(patient)
        self.save_patients()

    def show_patients(self):
        for patient in self.patients:
            print(patient)
            print()

    def find_patient(self, name):
        for existing_patient in self.patients:
            if existing_patient.name == name:
                return existing_patient
        return None

    def change_status(self, name, new_status):
        for existing_patient in self.patients:
            if existing_patient.name == name:
                existing_patient.status = new_status
                self.save_patients()
                return existing_patient
            
        return None