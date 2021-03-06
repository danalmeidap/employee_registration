from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Gender(Enum):
    Male = 1
    Female = 2
    Non_binary = 3

    def __str__(self) -> str:
        return self.name


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    age: int
    gender: str
    wage: float
    admission: Optional[datetime] = Field(default_factory=datetime.now)

    @validator("wage")
    def validate_wage(cls, v, field):
        if v < 0:
            raise RuntimeError(f"{field.name} must be between greather then 0")
        return v
