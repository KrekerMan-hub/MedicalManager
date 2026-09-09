#=======================
# Менеджер пациент 3.0
#=======================

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent/ "medical.db"

def init_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            diagnosis TEXT
        );
    """)

    connection.commit()
    connection.close()

def add_patient(name, age, diagnosis):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO patients (name, age, diagnosis) VALUES (?, ?, ?);",
                        (name, age, diagnosis))

    connection.commit()
    connection.close()

def get_patients():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, age, diagnosis FROM patients ORDER BY id;")

    patients = cursor.fetchall()

    connection.close()

    return patients

def get_patient_by_id(patient_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, age, diagnosis FROM patients WHERE id = ?",
                   (patient_id,))

    patient = cursor.fetchone()

    connection.close()

    
    return patient

def update_diagnosis(patient_id, new_diagnosis):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("UPDATE patients SET diagnosis = ? WHERE id = ?;",
                   (new_diagnosis, patient_id))

    connection.commit()

    update = cursor.rowcount
    
    connection.close()

    return update > 0

def delete_patient(patient_id):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM patients WHERE id = ?;",
                   (patient_id,))

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted > 0


if __name__ == "__main__":
    init_db()

    test_id = get_patients()[-1][0]

    print(delete_patient(test_id))
    print(get_patient_by_id(test_id))
    print(delete_patient(test_id))