tasks = []

def created_tasks():
    task = input("What's the task?")

    tasks.append(task)

def update_task():
    for index in range(len(tasks)):
        print(index + 1, "", task[index])

    index = int(input("\nwhich task do you want to update(please pick number)"))

    updated_task = input("update task: ")
    task[index - 1] = updated_task

def list_tasks():
    [print(task) for task in tasks]

def delete_task():
    for index in range(len(tasks)):
        print(index + 1, "", tasks[index])

    index = int(input("\nwhich task to you want to delete(please pick number)"))
    tasks.pop(index - 1)

def perform_action():
    if action == 1:
        create_task()
    elif action == 2:
        update_task
    elif action == 3:
        list_tasks()
    elif action == 4:
        delete_task()
    else:
        print("\nI'm sorry, but you must choose a number that's listed.")

def display_menu():
    actions = ["1. create a task", "2. update a task", "3. list all tasks", "4. delete a task", "5. exit"]
    print("\n")
    print("Todo List")
    print("=========\n")
    print("What would you like to do? (please select a number)\n\n")
    
    [print(action) for action in actions]
    entry = int(input(''))
    return entry

def main():
    entry = ""
    while entry != 5:
        entry = display_menu()
        if entry == 5:
            continue
        perform_action(entry)

if __name__ == "__main__":
    main()




