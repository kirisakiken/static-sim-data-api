from sqlalchemy import Column, String

from src.database.database_manager import Base


class WorldModel(Base):
    __tablename__ = "worlds"

    id = Column(String, primary_key=True)
    name = Column(String)
