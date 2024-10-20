from sqlmodel import Session
from sqlalchemy import text  
from db.models import Tour, Departure
from db import Config

def populate_mock_data():
    departures = [
        Departure(name="Париж", city="Paris"),
        Departure(name="Лондон", city="London"),
        Departure(name="Нью-Йорк", city="New York"),
        Departure(name="Токіо", city="Tokyo")
    ]
    
    with Session(Config.engine) as session:
        existing_departures = session.execute(text("SELECT COUNT(*) FROM departure")).first() #existing_departures = session.exec(text("SELECT COUNT(*) FROM departure")).first()
        
        if existing_departures[0] == 0: 
            for dep in departures:
                session.add(dep)
            session.commit() 

            mock_tours = Tour.mock_data(departures)
            for tour in mock_tours:
                session.add(tour)
            session.commit()

            for tour in mock_tours:
                print(f"Вставка туру: {tour.name}, відправлення: {tour.departure_id}")
                session.add(tour)
            session.commit()

        else:
            print("Дані вже існують у базі.")


if __name__ == "__main__":
    populate_mock_data()
    print("Тестові дані успішно додані.")