from sqlmodel import SQLModel, Field
from decimal import Decimal
from .departure import Departure
from typing import List

class Tour(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    desc: str
    price: Decimal
    image: str
    departure_id: int

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
                price=Decimal("10000.00"),
                image=images[0].id,
                departure_id=departures[0].id
            ),
            Tour(
                id=2,
                name="Тур до Риму",
                desc="Подорож до Вічного міста з Львова",
                price=Decimal("12000.00"),
                image=images[1].id,
                departure_id=departures[1].id
            ),
            Tour(
                id=3,
                name="Тур до Берліна",
                desc="Подорож до столиці Німеччини з Чернівців",
                price=Decimal("9000.00"),
                image=images[2].id,
                departure_id=departures[2].id
            )
        ]
        return tours