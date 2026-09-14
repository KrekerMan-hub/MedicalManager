#=======================
# Менеджер пациент 3.0
#=======================

import sqlite3
from pathlib import Path
from models import Patient


DB_PATH = Path(__file__).parent/ "medical.db"

class DatabaseConnection:
    def __enter__(self):
        self.connection = sqlite3.connect(DB_PATH)
        return self.connection

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
        finally:
            self.connection.close()


def init_db() -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                diagnosis TEXT
            );
        """)

def add_patient(name: str, age: int, diagnosis: str) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO patients (name, age, diagnosis) VALUES (?, ?, ?);",
                        (name, age, diagnosis))
        

def get_patients() -> list[Patient]:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT id, name, age, diagnosis FROM patients ORDER BY id;")

        rows = cursor.fetchall()

    return [Patient(*row) for row in rows]

def get_patient_by_id(patient_id: int) -> Patient | None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT id, name, age, diagnosis FROM patients WHERE id = ?",
                   (patient_id,))

        row = cursor.fetchone()

    if row is None:
        return None
    return Patient(*row)
    

def update_diagnosis(patient_id: int, new_diagnosis: str) -> bool:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE patients SET diagnosis = ? WHERE id = ?;",
                   (new_diagnosis, patient_id))

        update = cursor.rowcount
    
    return update > 0

def delete_patient(patient_id: int) -> bool:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM patients WHERE id = ?;",
                   (patient_id,))

        deleted = cursor.rowcount

    return deleted > 0


if __name__ == "__main__":
    init_db()