from sqlmodel import create_engine

class Config:
    DATABASE_URL = "sqlite:///database.db"
    
    engine = create_engine(DATABASE_URL, echo=True)
