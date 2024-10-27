from sqlmodel import SQLModel, Field, Relationship 
from typing import List  

class Departure(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    city: str
    tours: List["Tour"] = Relationship(back_populates="departure") 

    @staticmethod
    def mock_data() -> List['Departure']:
        return [
            Departure(id=1, name="Київ", city="Kyiv"), 
            Departure(id=2, name="Львів", city="Lviv"), 
            Departure(id=3, name="Чернівці", city="Chernivtsi"),  
        ]

class Tour(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    desc: str
    price: float
    image: str
    departure_id: int = Field(foreign_key="departure.id") 
    departure: Departure = Relationship(back_populates="tours")  

    @staticmethod
    def mock_data(departures: List[Departure]) -> List['Tour']:
        images = [
            "https://scc.losrios.edu/shared/img/body-misc/study-abroad/paris-france-night.jpg",
            "https://www.voyagetips.com/wp-content/uploads/2017/05/colisee-rome-840x486.jpg",
            "https://www.civitatis.com/f/alemania/berlin/berlin.jpg"
        ]
        tours = [
            Tour(
                id=1,
                name="Тур до Парижа",
                desc="Подорож до столиці Франції з Києва",
                price=10000.00,
                image=images[0],
                departure_id=departures[0].id
            ),
            Tour(
                id=2,
                name="Тур до Риму",
                desc="Подорож до Вічного міста з Львова",
                price=12000.00,
                image=images[1],
                departure_id=departures[1].id
            ),
            Tour(
                id=3,
                name="Тур до Берліна",
                desc="Подорож до столиці Німеччини з Чернівців",
                price=9000.00,
                image=images[2],
                departure_id=departures[2].id
            )
        ]
        return tours