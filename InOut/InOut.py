#In/Out Class Program
# [['name', 'status], [], []]
import Person

available_status = []

def update_status():
    for index in range (len(available_status)):
        print(index + 1, "", available_status[index][0])

    index = int(input("\nwhich employee do you want to update(please pick a number)"))
    updated_status = input("update status: ")

    employee = available_status[index - 1]
    employee[1] = updated_status

def list_employee():
    [print(employee.get_first_name(), "is", employee.get_status()) for employee in available_status]

def add_employee():
    name = input('name: ')
    status = input('current status: ')

    employee = Person.Person(name, status)
    available_status.append(employee)

def delete_emplayee():
    for index in range(len(available_status)):
        print(index + 1 , "", available_status[index][0])

    index = int(input("\nwhich imployee do you want to delete(please pick number)"))
    available_status.pop(index - 1)

def display_menu():
    actions = ["1. add employee", "2. update status", "3. delete employee", "4. list employee","e. exit"]
    print("\n")
    print("In / Out")
    print("==========\n")
    print("what would you like to do? (please select a number)\n\n")
    [print(action) for action in actions]

    entry = int(input(''))
    return entry

def perform_action(action):
    if action == 1:
        add_employee()
    elif action == 2:
        update_status()
    elif action == 3:
        delete_emplayee()
    elif action == 4:
        list_employee()
    else:
        print("\nI'm sorry, but you must choose a number that's listed.")

def main():
    entry = ""
    while entry !=5:
        entry = display_menu()
        if entry == 5:
            continue
        perform_action(entry)

if __name__ == "__main__":
    main()
