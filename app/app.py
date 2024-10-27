from flask import Flask, render_template
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import text
from db.models import Tour, Departure
from db.helpers import AutoincrementID
#from sqlmodel import Session
from config import Config
from populate_data import populate_mock_data


app = Flask(__name__)


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
    populate_mock_data()
    app.run(debug=True)