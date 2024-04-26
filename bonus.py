import json
from datetime import datetime

def save_to_do_list(todo_list):
    with open("to_do.json", "w") as file:
        json.dump(todo_list, file)

def load_to_do_list():
    try:
        with open("to_do.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_todo_item(title, date_time, done=False):
    todo_list = load_to_do_list()
    todo_item = {
        "title": title,
        "date_time": date_time,
        "done": done
    }
    todo_list.append(todo_item)
    save_to_do_list(todo_list)

def list_todo_items():
    todo_list = load_to_do_list()
    if not todo_list:
        print("Your To-Do list is empty.")
        return
    for idx, item in enumerate(todo_list, 1):
        status = "DONE" if item["done"] else "NOT DONE"
        print(f"{idx}- {item['title']} - {item['date_time']} - {status}")

def mark_as_done(task_index):
    todo_list = load_to_do_list()
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["done"] = True
        save_to_do_list(todo_list)
        print("Task marked as done.")
    else:
        print("Invalid task index.")

def search_task_by_title(title):
    todo_list = load_to_do_list()
    found_tasks = [task for task in todo_list if task["title"].lower() == title.lower()]
    if found_tasks:
        for idx, task in enumerate(found_tasks, 1):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{idx}- {task['title']} - {task['date_time']} - {status}")
    else:
        print("No tasks found with that title.")

def main():
    while True:
        print("\n1- Add a new To-Do item")
        print("2- List To-Do items")
        print("3- Mark a task as done")
        print("4- Search tasks by title")
        print("5- Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter the title of the task: ")
            date_time_str = input("Enter date & time (YYYY-MM-DD HH:MM:SS): ")
            date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
            add_todo_item(title, date_time)
        elif choice == "2":
            print("Your To-Do items:")
            list_todo_items()
        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as done: "))
            mark_as_done(task_index)
        elif choice == "4":
            search_title = input("Enter the title to search for: ")
            search_task_by_title(search_title)
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
