#=========================
# Меню
#=========================

from patient import (Patient, Department, PatientStatus)

def main_menu():
    print("====== Medicat Patient Manager ======")
    print("1. Показать пациентов.")
    print("2. Добавить пациента.")
    print("3. Найти пациента.")
    print("4. Изменить статус пациента.")
    print("0. Выход")

def find_patient_menu(hospital):
    name = input("Введите имя пациента: ").strip().title()
    patient = hospital.find_patient(name)

    if patient:
        print(patient)
        print()
    else:
        print("Пациент не найден.\n")

def chosie_department():
    print("Список отделений.")
    print("1. Терапия.")
    print("2. Хирургия.")
    print("3. Реанимация.")
    departament = input("Выберите отделение: ")
    if departament == "1":
        return Department.THERAPY
    elif departament == "2":
        return Department.SURGERY
    elif departament == "3":
        return Department.ICU
    else:
        print("Нет такого отделения.\n")
    
def creat_patient():
    name = input("Введите имя пациента: ").strip().title()
    if not name:
        print("Имя не может быть пустым")
        return None
    try:
        age = int(input("Введите возраст пациента(число): "))
        if not age:
            print("Возраст не может быть пустым.")
            return None
    except ValueError:
        print("Введите число")
        return None
    diagnosis = input("Введите диагноз пациента: ").strip().title()
    if not diagnosis:
        print("Диагноз не может быть пустым.")
        return None
    department = chosie_department()
    if department is None:
        return None
    status = PatientStatus.ADMITTED
    patient = Patient(name, age, diagnosis, department, status)
    return patient


def change_status_menu(hospital):
    name = input("Введите имя пациента: ").strip().title()
    print()
    print("Статус.")
    print("1. Госпитализирован")
    print("2. Выписан")
    print("3. Переведён.")

    new_status = input("Выберите новый статус: ")
    if new_status == "1":
        new_status = PatientStatus.ADMITTED
    elif new_status == "2":
        new_status = PatientStatus.DISCHARGED
    elif new_status == "3":
        new_status = PatientStatus.TRANSFERRED
    else:
        print("Нет такого статуса.\n")
        return
    
    patient = hospital.change_status(name, new_status)

    if patient:
        print("Статус изменён.\n")
    else:
        print("Пациент не найден.\n")
