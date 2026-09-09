#======================
# Основное меню
#======================

from database import init_db, get_patients, add_patient, get_patient_by_id, update_diagnosis, delete_patient

def main():
    init_db()

    while True:
        print("\n=== Менеджер пациентов 3.0 ===")
        print("1. Показать всех пациентов")
        print("2. Добавть пациента")
        print("3. Найти пациента по ID")
        print("4. Изменение диагноза.")
        print("5. Удаление пациента.")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        #Список пациентов
        if choice == "1":
            patients = get_patients()
            if not patients:
                print("Список пациентов пуст.")
            else:
                for patient_id, name, age, diagnosis in patients:
                    print(f"ID: {patient_id} | Имя: {name}, возраст: {age}\nДиагноз: {diagnosis}\n")

        #Добавит пациента
        elif choice == "2":
            name = input("Введите имя пациента: ").strip().title()
            if not name:
                print("Имя не может быть пустым.")
                continue
            try:
                age = int(input("Введите возраст пациента(число): "))
            except ValueError:
                print("Неккоректное введение данных.")
                continue
            if age < 0 or age > 120:
                print("Возраст должен быть от 0 до 120.")
                continue
            diagnosis = input("Введите диагноз пациента: ").strip()
            if not diagnosis:
                print("Диагноз не может быть пустым.")
                continue
            add_patient(name, age, diagnosis)
            print("Пациент успешно добавлен.")

        #Поиск по ID
        elif choice == "3":
            try:
                patient_id = int(input("Введите ID пациента: "))
            except ValueError:
                print("Неккоректное введение данных.")
                continue
            patient = get_patient_by_id(patient_id)
            if patient is None:
                print("Пациент не найден.")
            else:
                print(f"ID: {patient[0]} | Имя: {patient[1]}, возраст: {patient[2]}\nДиагноз: {patient[3]}\n")


        # Изменить диагноз
        elif choice == "4":
            try:
                patient_id = int(input("Введите ID пациента: "))
            except ValueError:
                print("Неккоректное введение данных.")
                continue
            patient = get_patient_by_id(patient_id)
            if patient is None:
                print("Пациент не найден.")
            else:
                print(f"Текущий диагноз: {patient[3]}\n")
                new_diagnosis = input("Введите новый диагноз: ").strip()
                if not new_diagnosis:
                    print("Диагноз не может быть пустым.")
                    continue
                update = update_diagnosis(patient_id, new_diagnosis)
                if update:
                    print("Диагноз изменен.")
                else:
                    print("Пациент не найден")

        # Удаление пациентв
        elif choice == "5":
            try:
                patient_id = int(input("Введите ID пациента: "))
            except ValueError:
                print("Неккоректное введение данных.")
                continue
            patient = get_patient_by_id(patient_id)
            if patient is None:
                print("Пациент не найден.")
            else:
                confirmation = input(f"Удалить пациента: {patient[1]}? Введите «да»/«нет»: ").strip().lower()
                if confirmation != "да":
                    print("Удаление отменено.")
                    continue
                delete = delete_patient(patient_id)
                if delete:
                    print("Пациент удалён.")
                else:
                    print("Пациент не найден.")


        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Нет такого пункта меню.")


if __name__ == "__main__":
    main()