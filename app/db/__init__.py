from sqlmodel import SQLModel, create_engine, Session


from . import models


class Config:
    engine = create_engine("sqlite:///my_database.sql")
    session = Session(bind=engine)