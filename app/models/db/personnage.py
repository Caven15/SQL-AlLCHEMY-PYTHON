from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .personnage_quete import personnage_quete

class Personnage(Base):
	__tablename__ = 'personnage'

	id = Column(Integer,primary_key=True)
	nom = Column(String, nullable=False)

    # FK vers Race
	race_id = Column(Integer, ForeignKey("race.id"))
	race = relationship("Race", back_populates="personnage")

    # Relation 1:1 avec anneau
	anneau = relationship("Anneau", back_populates="proprietaire", uselist=False)

	# Relation N:N avec quete
	quetes = relationship("Quete", secondary=personnage_quete, back_populates="participants")