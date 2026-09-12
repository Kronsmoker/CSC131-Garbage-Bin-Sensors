from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import random
from datetime import datetime

from database import SessionLocal
from models.reading import SensorReading

router = APIRouter(
    prefix="/sensors",
    tags=["Sensors"]
)

# Gives this route a connection to PostgreSQL
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/fake-reading")
def fake_sensor_reading(db: Session = Depends(get_db)):

    # Fake distance measured by ultrasonic sensor
    distance_cm = round(random.uniform(5, 80), 1)

    # Distance when the bin is completely empty
    empty_distance_cm = 80

    # Calculate how full the bin is
    fill_percent = round(
        ((empty_distance_cm - distance_cm) / empty_distance_cm) * 100
    )

    # Fake battery level
    battery_percent = random.randint(60, 100)

    # Create a sensor reading for PostgreSQL
    reading = SensorReading(
        sensor_id="BIN-001",
        distance_cm=distance_cm,
        fill_percent=fill_percent,
        battery_percent=battery_percent,
        timestamp=datetime.now()
    )

    # Save the reading
    db.add(reading)
    db.commit()
    db.refresh(reading)

    return {
        "id": reading.id,
        "sensor_id": reading.sensor_id,
        "distance_cm": reading.distance_cm,
        "fill_percent": reading.fill_percent,
        "battery_percent": reading.battery_percent,
        "timestamp": reading.timestamp
    }

