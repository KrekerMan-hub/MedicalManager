#=============================
# Основа для запуска
#============================+

from patient import (Patient, Department, PatientStatus)
from hospital import Hospital
from menu import (find_patient_menu, chosie_department, creat_patient, change_status_menu, main_menu)

def main():
    hospital = Hospital("Day41/patients.json")
    hospital.load_patients()
    while True:
        main_menu()
        print()
        choise = input("Выберите действие: ")

        if choise == "0":
            break

        elif choise == "1":
            hospital.show_patients()

        elif choise == "2":
            patient = creat_patient()
            if patient:
                hospital.add_patient(patient)

        elif choise == "3":
            find_patient_menu(hospital)

        elif choise == "4":
            change_status_menu(hospital)

        else:
            print("Нет такого выбора.")

if __name__ == "__main__":
    main()