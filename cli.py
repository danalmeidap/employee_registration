from time import sleep
from typing import List

from rich import print
from rich.console import Console
from rich.table import Table

from core import (
    add_employee_to_database,
    delete_employee_from_database,
    get_employee_from_database,
    get_employees_from_database,
    update_employee_age,
    update_employee_wage,
)
from models import Employee, Gender
from operations import (
    validate_age,
    validate_gender,
    validate_index,
    validate_wage,
)


def employee_register() -> None:
    """Add Employee to database"""
    name: str = str(input("Employee's Name: ")).title()
    age: int = int(input("Employee's Age: "))
    gender: int = validate_gender(
        "Employee Gender: type 1 to male, 2- for female, 3- for non binary"
    )
    wage: float = float(input("Employee's Wage: "))
    if add_employee_to_database(name, age, Gender(gender).name, wage):
        print("Employee was added sucefully")
    else:
        print("Cannot add employee.")
    sleep(2)
    menu()


def employee_list() -> None:
    """List employees from database"""
    employees: List[Employee] = get_employees_from_database()
    if len(employees) > 0:
        table = generate_employee_table(employees)
        console.print(table)
    else:
        print("Employees list is empty")
    sleep(2)
    menu()


def search_employee_by_id() -> None:
    """Search a employee by id"""
    employees: List[Employee] = get_employees_from_database()
    if len(employees) > 0:
        employees_id: int = validate_index("Index for searching: ")
        employee: List[Employee] = get_employee_from_database(employees_id)
        table: Table = generate_employee_table(employee)
        console.print(table)
    else:
        print("Employees list is empty")
    sleep(2)
    menu()


def update_wage() -> None:
    """Update employee's wage"""
    employees: List[Employee] = get_employees_from_database()
    if len(employees) > 0:
        employee_id: int = validate_index("Index for searching: ")
        new_wage: float = validate_wage("New wage: ")
        employee: List[Employee] = update_employee_wage(employee_id, new_wage)
        table: Table = generate_employee_table(employee)
        console.print(table)
    else:
        print("Employees list is empty")
    sleep(2)
    menu()


def update_age() -> None:
    """Update employee's age"""
    employees: List[Employee] = get_employees_from_database()
    if len(employees) > 0:
        employee_id: int = validate_index("Index for searching: ")
        new_age: int = validate_age("New wage: ")
        employee: List[Employee] = update_employee_age(employee_id, new_age)
        table: Table = generate_employee_table(employee)
        console.print(table)
    else:
        print("Employees list is empty")
    sleep(2)
    menu()


def delete_employee() -> None:
    """Delete employee from database"""
    employees: List[Employee] = get_employees_from_database()
    if len(employees) > 0:
        employee_id: int = validate_index("Index for searching: ")
        if delete_employee_from_database(employee_id):
            print("The employee was deleted")
        else:
            print("Operation not concluded")
    else:
        print("Employees list is empty")
    sleep(2)
    menu()


def generate_employee_table(employee: List[Employee]) -> Table:
    table: Table = Table(title="Employees Database")
    headers: List[str] = [
        "id",
        "name",
        "age",
        "gender",
        "wage",
        "admission",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for employee in employee:
        employee.admission = employee.admission.strftime("%Y-%m-%d")
        values: List[str] = [
            str(getattr(employee, header)) for header in headers
        ]
        table.add_row(*values)
    return table


def menu() -> None:
    print("Selecione uma opção no menu: ")
    print("1 - Employee register")
    print("2 - Employee's list")
    print("3 - Search employee by id")
    print("4 - Update Wage")
    print("5 - Update Age")
    print("6 - Delete Employee")
    print("7 - Exit")

    option: int = int(input())

    if option == 1:
        employee_register()
    elif option == 2:
        employee_list()
    elif option == 3:
        search_employee_by_id()
    elif option == 4:
        update_wage()
    elif option == 5:
        update_age()
    elif option == 6:
        delete_employee()
    elif option == 7:
        print("Thank You!!")
        sleep(2)
        exit(0)
    else:
        print("Invalid Operationj")
        sleep(2)
        menu()


console = Console()
