from sqlmodel import Session, SQLModel
from sqlalchemy import text  
from db.models import Tour, Departure
from db import Config
from sqlalchemy import select

def populate_mock_data():
    SQLModel.metadata.drop_all(Config.engine)
    SQLModel.metadata.create_all(Config.engine)
    

    with Session(Config.engine) as session:
        departures = Departure.mock_data()
        tours = Tour.mock_data(departures)
        session.add_all(departures)
        session.commit() 

if __name__ == "__main__":
    populate_mock_data()
    print("Тестові дані успішно додані.")