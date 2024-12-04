from pydantic import BaseModel, Field

class Vehicle(BaseModel):
    vin: str = Field(..., description="Vehicle Identification Number")
    manufacturer_name: str
    description: str
    horse_power: int = Field(..., ge=0, description="Horsepower, non-negative")
    model_name: str
    model_year: int = Field(..., gt=1900, description="Model year, 1900 or later")
    purchase_price: float = Field(..., gt=0, description="Price, positive")
    fuel_type: str

    class Config:
        orm_mode = True  # For SQLAlchemy model compatibility
