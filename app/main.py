from init_db import session, db_connected

if db_connected:
    print("Prêt pour la logique métier....")
else:
    print("La base de donne n'est pas connectée")