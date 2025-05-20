from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .personnage_quete import personnage_quete

class Quete(Base):
    __tablename__ = 'quete'

    id = Column(Integer, primary_key=True)
    titre = Column(String, nullable=False)

    # Relation N:N avec Personnages
    participants = relationship("Personnage", secondary=personnage_quete, back_populates="quete")
