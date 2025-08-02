import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Введите новую задачу: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Задача добавлена.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Удалена задача: {removed}\n")
        else:
            print("Некорректный номер.\n")
    except ValueError:
        print("Введите правильное число.\n")

def clear_tasks():
    confirm = input("Удалить все задачи? (y/n): ").lower()
    if confirm == "y":
        save_tasks([])
        print("Все задачи удалены.\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Очистить все задачи")
        print("5. Выход\n")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            clear_tasks()
            tasks = []
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.\n")

if __name__ == "__main__":
    main()
