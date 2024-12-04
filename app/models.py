from sqlalchemy import Column, String, Integer, Text, Float
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    vin = Column(String(17), primary_key=True, index=True)
    manufacturer_name = Column(String(255), nullable=False)
    description = Column(Text)
    horse_power = Column(Integer, nullable=False)
    model_name = Column(String(255), nullable=False)
    model_year = Column(Integer, nullable=False)
    purchase_price = Column(Float, nullable=False)
    fuel_type = Column(String(50), nullable=False)
