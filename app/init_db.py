from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from config import URL_DB

# import des modèles...
from models.db.base import Base
from models.db import race, personnage, anneau, quete, personnage_quete


# initialisation des objets
engine = None
session = None
db_connected = False

try:
	# Connexion à la base de donnée 
	engine = create_engine(URL_DB)

	# Initialisation d'une session
	session = sessionmaker(bind=engine)
	session = session()

	# Base.metadata.drop_all(bind=engine)

	# Création des tables si elles n'existent pas 
	Base.metadata.create_all(bind=engine)

	db_connected = True
	print("-----------------------")
	print("Connexion DB + modèles créer")
	print("-----------------------")
except SQLAlchemyError as e:
    print("Erreur lors de la connexion à la base de donnée :")
    print(e)