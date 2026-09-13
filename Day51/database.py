#=======================
# Менеджер пациент 3.0
#=======================

import sqlite3
from pathlib import Path
from models import Patient

type PatientRow = tuple[int, str, int | None, str | None]

DB_PATH = Path(__file__).parent/ "medical.db"

def init_db() -> None:
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

def add_patient(name: str, age: int, diagnosis: str) -> None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO patients (name, age, diagnosis) VALUES (?, ?, ?);",
                        (name, age, diagnosis))

    connection.commit()
    connection.close()

def get_patients() -> list[PatientRow]:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, age, diagnosis FROM patients ORDER BY id;")

    rows = cursor.fetchall()

    connection.close()

    return (Patient(*row) for row in rows)

def get_patient_by_id(patient_id: int) -> Patient | None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, age, diagnosis FROM patients WHERE id = ?",
                   (patient_id,))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None
    return Patient(*row)
    

def update_diagnosis(patient_id: int, new_diagnosis: str) -> bool:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("UPDATE patients SET diagnosis = ? WHERE id = ?;",
                   (new_diagnosis, patient_id))

    connection.commit()

    update = cursor.rowcount
    
    connection.close()

    return update > 0

def delete_patient(patient_id: int) -> bool:
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