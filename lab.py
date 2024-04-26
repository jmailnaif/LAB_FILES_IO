def add_todo_item(todo_item):
    with open("to_do.txt", "a") as file:
        file.write(todo_item + "\n")

def list_todo_items():
    with open("to_do.txt", "r") as file:
        todo_list = file.readlines()
        for item in todo_list:
            print(item.strip())

def main():
    while True:
        add_new = input("Do you want to add a new To-Do item? (y/n): ")
        if add_new.lower() == "y":
            new_item = input("Enter your new To-Do item: ")
            add_todo_item(new_item)
        elif add_new.lower() == "n":
            list_items = input("Do you want to list your To-Do items? (y/n): ")
            if list_items.lower() == "y":
                print("Your To-Do items:")
                list_todo_items()
        exit_program = input("Type 'exit' to exit or press Enter to continue: ")
        if exit_program.lower() == "exit":
            print("Thank you for using the To-Do program. Come back again soon!")
            break

if __name__ == "__main__":
    main()
