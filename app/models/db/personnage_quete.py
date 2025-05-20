from sqlalchemy import Table, Column, ForeignKey
from .base import Base

# Table d'association Many-to-Many entre Personnage et Quete
personnage_quete = Table(
    'personnage_quete',
    Base.metadata,
    Column('personnage_id', ForeignKey('personnage.id'), primary_key=True),
    Column('quete_id', ForeignKey('quete.id'), primary_key=True)
)
