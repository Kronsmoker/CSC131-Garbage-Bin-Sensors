from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database import Base


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)

    sensor_id = Column(String, nullable=False)

    distance_cm = Column(Float, nullable=False)

    fill_percent = Column(Integer, nullable=False)

    battery_percent = Column(Integer, nullable=False)

    timestamp = Column(
        DateTime,
        default=datetime.now
    )