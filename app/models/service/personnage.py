from sqlalchemy import text
from models.db.personnage import Personnage as PersonnageModel
from .db_tools import DBTools  # outil de base pour session + commit

class Personnage(DBTools):
    """
    Classe représentant la logique de gestion des personnages.
    Utilise à la fois SQLAlchemy ORM et requêtes SQL brutes.
    Hérite de DBTools pour la session et les transactions.
    """

    def __init__(self, session):
        super().__init__(session)

    # --- MÉTHODES ORM ---

    def ajouter(self, nom, race):
        perso = PersonnageModel(nom=nom, race=race)
        self.session.add(perso)
        self.commit()
        return perso

    def lister(self):
        return self.session.query(PersonnageModel).all()

    def chercher_par_id(self, id_):
        return self.session.query(PersonnageModel).filter_by(id=id_).first()

    def chercher_par_nom(self, nom):
        return self.session.query(PersonnageModel).filter(
            PersonnageModel.nom.ilike(f"%{nom}%")
        ).all()

    def avec_quetes(self):
        return (
            self.session.query(PersonnageModel)
            .join(PersonnageModel.quetes)
            .distinct()
            .all()
        )

    def ayant_anneau(self):
        return self.session.query(PersonnageModel).filter(PersonnageModel.anneau != None).all()

    def modifier(self, id_, nouveau_nom):
        p = self.chercher_par_id(id_)
        if p:
            p.nom = nouveau_nom
            self.commit()
        return p

    def supprimer(self, id_):
        p = self.chercher_par_id(id_)
        if p:
            self.session.delete(p)
            self.commit()
            return True
        return False

    def afficher_details(self, perso):
        print(f"\n👤 {perso.nom}")
        print(f"Race : {perso.race.nom}")
        print(f"Anneau : {perso.anneau.nom if perso.anneau else 'Aucun'}")
        print("Quêtes :")
        for q in perso.quetes:
            print(f" - {q.titre}")
