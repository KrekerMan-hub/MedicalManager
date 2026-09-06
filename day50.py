#========================
# Работа с SQL и Python
#========================

import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "medical.db"

if db_path.exists():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    patient_id = int(input("Введите ID пациента: "))
    patient_new_diagnosis = input("Введите новый диагноз пациента: ")

    cursor.execute("UPDATE patients SET diagnosis = ? WHERE id = ?;",
                   (patient_new_diagnosis, patient_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("Пациент с таком ID не найден")
    else:
        print("Диагноз успешно изменен")

    
    print(f"Добавлен пациент: {cursor.lastrowid}")
    
    cursor.execute("SELECT * FROM patients;")

    patients = cursor.fetchall()

    for patient in patients:
        print(f"ID: {patient[0]} | Пациент: {patient[1]}, возраст: {patient[2]} - {patient[3]}")

    connection.close()

else:
    print("Файл базы не найден. Проверь имя и расположение")