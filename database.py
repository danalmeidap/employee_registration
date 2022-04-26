from sqlmodel import create_engine
import models

engine = create_engine("sqlite:///employee.db", echo=False)
models.SQLModel.metadata.create_all(engine)