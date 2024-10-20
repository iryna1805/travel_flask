from sqlmodel import SQLModel, Field


class AutoincrementID(SQLModel, table=False):
    id: int | None = Field(primary_key=True, default=None)