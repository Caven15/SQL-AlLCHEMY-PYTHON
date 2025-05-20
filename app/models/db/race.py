from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Race(Base):
	__tablename__ = 'race'

	id = Column(Integer,primary_key=True)
	nom = Column(String, nullable=False)

	# Une race peut avoir plusieurs personnages
	personnage = relationship("Personnage", back_populates="race")