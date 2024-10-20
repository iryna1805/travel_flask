from sqlmodel import SQLModel, Field
from typing import List
from models import Departure

class Departure(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    city: str

    @staticmethod
    def mock_data() -> List['Departure']:
        return [
            Departure(id=1, name="Київ", city="Kyiv"),
            Departure(id=2, name="Львів", city="Lviv"),
            Departure(id=3, name="Чернівці", city="Chernivtsi"),
        ]
