from flask import Flask, render_template
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import text
from db.models import Tour, Departure
from db.helpers import AutoincrementID
#from sqlmodel import Session
from config import Config


app = Flask(__name__)

def populate_mock_data():
    departures = [
        Departure(name="Париж", city="Paris"),
        Departure(name="Лондон", city="London"),
        Departure(name="Нью-Йорк", city="New York"),
        Departure(name="Токіо", city="Tokyo")
    ]
    
    with Session(Config.engine) as session:
        existing_departures = session.execute(text("SELECT COUNT(*) FROM departure")).first()
        
        if existing_departures[0] == 0:  
            for dep in departures:
                session.add(dep)
            session.commit() 

            mock_tours = Tour.mock_data(departures)
            for tour in mock_tours:
                session.add(tour)
            session.commit() 
        else:
            print("Дані вже існують у базі.")


@app.get("/")
def index():
    with Session(Config.engine) as session:
        tours = session.query(Tour).all()
    return render_template("index.html", tours=tours)

@app.get("/tour/<int:tour_id>")
def tour_detail(tour_id):
    with Session(Config.engine) as session:
        tour = session.query(Tour).options(joinedload(Tour.departure)).filter(Tour.id == tour_id).first() #tour = session.query(Tour).filter(Tour.id == tour_id).first()  #tour = session.get(Tour, tour_id) 
        if not tour:
            return "Тур не знайдено", 404
    return render_template("tour_detail.html", tour=tour)

if __name__ == "__main__":
    with Config.engine.begin() as conn:
        AutoincrementID.metadata.create_all(conn)

    print("Таблиці створено успішно.")
    populate_mock_data()
    app.run(debug=True)