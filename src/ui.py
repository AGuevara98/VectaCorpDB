# UI layer
from objects import Employee
import db
#import Employee


def display_menu():
    print('The Vecta Corp Help Desk Application (Admin) \n')
    print('COMMAND MENU')
    print('-' * 40)
    print('view - View all employees')
    print('add - Add an employee')
    print('del - Remove an employee')
    print('exit - Exit the program')
    print('-' * 40)
    
def view_employees():
    print("")
    print("VECTA CORP HELP DESK EMPLOYEES")
    print("-" * 85)
    line_format = "{:5s} {:15s} {:15s} {:15s} {:25s} {:5s}"
    print(line_format.format("ID", "Name", "Username", "Password", "Email", "Role"))
    print("-" * 85)
    employees = db.get_employees()
    for employee in employees:
        print(line_format.format(str(employee.employeeid), employee.name,
                                     employee.username, employee.password,
                                     employee.email, str(employee.roleid)))
    print("-" * 85)
    
def add_employee():
    name = input("Name: ")
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    roleid = int(input("Role ID: "))
    
    employee = Employee(name=name, username=username, password=password, email=email, roleid=roleid)
    db.add_employee(employee)
    print(name + " was added successfully to the database!\n")
    
def delete_employee():
    employeeid = int(input("Employee ID: "))
    employee = db.get_employee(employeeid)
    choice = input("Are you sure you want to delete '" + employee.name + "'? (y/n): ")
    if (choice == "y"):
        db.delete_employee(employeeid)
        print("'" + employee.name + "' was deleted succesfully.\n")
    else:
        print("'" + employee.name + "' was not deleted.\n")
    
def main():
    db.connect()
    display_menu()
    
    while True:
        command = input('Enter command: ')
        
        if command == "view":
            view_employees()
        elif command == "add":
            add_employee()
        elif command == "delete":
            delete_employee()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()

    db.close()
    print("The program has been terminated")
    
if __name__ == "__main__":
    main()