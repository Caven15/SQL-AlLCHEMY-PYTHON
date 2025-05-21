from sqlalchemy import text
from .db_tools import DBTools  # import du helper commun

class Anneau(DBTools):
    """
    Classe Anneau – utilise exclusivement des requêtes SQL brutes.
    Hérite de DBTools pour gérer la session et le commit.
    """

    def __init__(self, session):
        super().__init__(session)

    def lister(self):
        """
        Affiche tous les anneaux avec leur porteur (s'il y en a un).
        LEFT JOIN permet d'afficher même ceux sans porteur.
        """
        result = self.session.execute(text("""
            SELECT a.id, a.nom AS anneau, p.nom AS porteur
            FROM anneaux a
            LEFT JOIN personnages p ON a.proprietaire_id = p.id
            ORDER BY a.id
        """))
        for row in result.fetchall():
            print(f"[{row.id}] {row.anneau} — porté par : {row.porteur or 'Aucun'}")

    def chercher_par_nom(self, nom):
        """
        Recherche un anneau par nom exact (sécurisé).
        """
        result = self.session.execute(
            text("SELECT * FROM anneaux WHERE nom = :nom"),
            {"nom": nom}
        )
        return result.fetchall()

    def ajouter(self, nom, proprietaire_id=None):
        """
        Ajoute un nouvel anneau en base.
        Si aucun propriétaire n’est précisé, la FK peut rester NULL.
        """
        self.session.execute(
            text("""
                INSERT INTO anneaux (nom, proprietaire_id)
                VALUES (:nom, :proprietaire_id)
            """),
            {"nom": nom, "proprietaire_id": proprietaire_id}
        )
        self.commit()
        print(f"✅ Anneau '{nom}' ajouté.")

    def supprimer_par_id(self, id_):
        """
        Supprime un anneau par ID.
        """
        self.session.execute(
            text("DELETE FROM anneaux WHERE id = :id"),
            {"id": id_}
        )
        self.commit()
        print(f"🗑️ Anneau avec ID {id_} supprimé.")
