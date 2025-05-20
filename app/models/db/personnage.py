from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Personnage(Base):
	__tablename__ = 'race'

	id = Column(Integer,primary_key=True)
	nom = Column(String, nullable=False)

	# ForeignKey vers Race
	id_race = Column()
 
 