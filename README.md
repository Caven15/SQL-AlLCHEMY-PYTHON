Création de l'environnement virtuel	=> 	py -3 -m venv .venv
						 Activation =>  .\.venv\Scripts\activate

scheme = "postgresql+psycopg2"
username = ""
password = ""
hostname = ""
port = ""
database_name = ""

URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"