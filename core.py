from typing import List

from sqlmodel import select

from database import get_session
from models import Employee


def add_employee_to_database(
    name: str, age: int, gender: str, wage: float
) -> bool:
    with get_session() as session:
        employee = Employee(**locals())
        session.add(employee)
        session.commit()
    return True


def get_employees_from_database() -> List[Employee]:
    with get_session() as session:
        sql = select(Employee)
        return list(session.exec(sql))


def get_employee_from_database(employee_id: int) -> List[Employee]:
    with get_session() as session:
        sql = select(Employee).where(Employee.id == employee_id)
        return list(session.exec(sql))


def update_employee_wage(employee_id: int, new_wage: float) -> List[Employee]:
    with get_session() as session:
        statement = select(Employee).where(Employee.id == employee_id)
        results = session.exec(statement)
        employee = results.one()
        employee.wage = new_wage
        sql = select(Employee).where(Employee.id == employee_id)
        session.commit()
        return list(session.exec(sql))


def update_employee_age(employee_id: int, new_age: int) -> List[Employee]:
    with get_session() as session:
        statement = select(Employee).where(Employee.id == employee_id)
        results = session.exec(statement)
        employee = results.one()
        employee.age = new_age
        sql = select(Employee).where(Employee.id == employee_id)
        session.commit()
        return list(session.exec(sql))


def delete_employee_from_database(employee_id: int) -> bool:
    with get_session() as session:
        statement = select(Employee).where(Employee.id == employee_id)
        results = session.exec(statement)
        employee = results.one()
        session.delete(employee)
        return True
