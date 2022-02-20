from datetime import datetime, timedelta
from sqlalchemy import Column, String, DateTime
from dataclasses import dataclass

from app.configs.database import db

@dataclass
class Vaccine(db.Model):
	__tablename__ = "vaccine_cards"
	date = datetime.now()

	cpf: str = Column(String(11), primary_key=True)
	name: str = Column(String, nullable=False)
	first_shot_date: str = Column(DateTime, default=date)
	second_shot_date: str = Column(DateTime, default=date + timedelta(days=90))
	vaccine_name: str = Column(String, nullable=False)
	health_unit_name: str = Column(String, nullable=False)