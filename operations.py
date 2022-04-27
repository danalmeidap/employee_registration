from sys import exit
from models import Employee
from typing import List
from core import get_employees_from_database


def validate_gender(msg: str) -> int:
    while True:
        try:
            gender: int = int(input(msg))
            if 1 <= gender <= 3:
                return gender
            else:
                print("Value must be between 1 and 3")
        except (TypeError, ValueError):
            print("Value must be between an integer")
        except KeyboardInterrupt:
            print("interrupted by user")
            exit(-1)


def validate_index(msg: str) -> int:
    employees: List[Employee] = get_employees_from_database()
    while True:
        try:
            index: int = int(input(msg))
            if 1 <= index <= len(employees):
                return index
            else:
                print("Index value does not exist in database")
        except (ValueError, TypeError):
            print("The value must be an integer")
        except KeyboardInterrupt:
            print("interrupted by user")
            exit(-1)


def validate_wage(msg: str) -> float:
    while True:
        try:
            wage: float = float(input(msg))
            if wage > 0:
                return wage
            else:
                print("Wage value must be greather then zero")
        except (ValueError, TypeError):
            print("The value must be a float number")
        except KeyboardInterrupt:
            print("interrupted by user")
            exit(-1)


def validate_age(msg: str) -> int:
    while True:
        try:
            age: int = int(input(msg))
            if age > 0:
                return age
            else:
                print("Age value must be greather then zero")
        except (ValueError, TypeError):
            print("The value must be an integer")
        except KeyboardInterrupt:
            print("interrupted by user")
            exit(-1)
