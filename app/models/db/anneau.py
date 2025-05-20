from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Anneau(Base):
    __tablename__ = 'anneau'

    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)

	# Lien 1:1 avec personnage
    id_proprietaire = Column(Integer, ForeignKey("personnage.id"))
    proprietaire = relationship("Personnage", back_populates="anneau", uselist=False)