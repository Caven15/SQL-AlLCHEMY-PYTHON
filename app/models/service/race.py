from models.db.race import Race as RaceModel
from .db_tools import DBTools

class Race(DBTools):
    def __init__(self, session):
        super().__init__(session)

    def peupler(self):
        """
        Insère les races emblématiques du Seigneur des Anneaux si la table est vide.
        """
        if self.session.query(RaceModel).first():
            print("⚠️ Les races existent déjà, aucun ajout.")
            return

        races = [
            RaceModel(nom="Humain"),
            RaceModel(nom="Elfe"),
            RaceModel(nom="Nain"),
            RaceModel(nom="Hobbit"),
            RaceModel(nom="Dunedain"),
            RaceModel(nom="Orc"),
        ]

        self.session.add_all(races)
        self.commit()
        print("✅ Races insérées.")

    def lister(self):
        """
        Retourne toutes les races en base.
        """
        return self.session.query(RaceModel).all()