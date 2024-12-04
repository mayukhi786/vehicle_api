from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import schemas, models, database
from typing import List

router = APIRouter()

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vehicle", response_model=List[schemas.Vehicle])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()

@router.post("/vehicle", response_model=schemas.Vehicle, status_code=201)
def create_vehicle(vehicle: schemas.Vehicle, db: Session = Depends(get_db)):
    try:
        db_vehicle = models.Vehicle(**vehicle.dict())
        db.add(db_vehicle)
        db.commit()
        db.refresh(db_vehicle)
        return db_vehicle
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Vehicle with VIN {vehicle.vin} already exists."
        )



@router.get("/vehicle/{vin}", response_model=schemas.Vehicle)
def get_vehicle(vin: str, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vin == vin).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.put("/vehicle/{vin}", response_model=schemas.Vehicle)
def update_vehicle(vin: str, vehicle: schemas.Vehicle, db: Session = Depends(get_db)):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.vin == vin).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    for key, value in vehicle.dict().items():
        setattr(db_vehicle, key, value)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.delete("/vehicle/{vin}", status_code=204)
def delete_vehicle(vin: str, db: Session = Depends(get_db)):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.vin == vin).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db.delete(db_vehicle)
    db.commit()
    return
