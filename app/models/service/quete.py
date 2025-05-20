from models.db.quete import Quete as QueteModel
from models.db.personnage import Personnage
from .db_tools import DBTools

class Quete(DBTools):
    def __init__(self, session):
        super().__init__(session)  # initialise self.session via DBTools

    def peupler(self):
        """
        Insère les quêtes emblématiques du Seigneur des Anneaux si la table est vide.
        """
        if self.session.query(QueteModel).first():
            print("⚠️ Les quêtes existent déjà, aucun ajout.")
            return

        quetes = [
            QueteModel(titre="Détruire l'Anneau Unique"),
            QueteModel(titre="La Bataille du Gouffre de Helm"),
            QueteModel(titre="La Communauté de l'Anneau"),
            QueteModel(titre="La Guerre de l'Anneau"),
            QueteModel(titre="Fuite de la Moria"),
            QueteModel(titre="Traversée de la Lothlorien"),
            QueteModel(titre="L'Ascension du Mordor"),
            QueteModel(titre="Défense du Gondor"),
            QueteModel(titre="La Reconquête de la Comté"),
            QueteModel(titre="Le Couronnement d'Aragorn"),
        ]

        self.session.add_all(quetes)
        self.commit()
        print("✅ Quêtes insérées.")


    def ajouter_personnage(self, quete_id, personnage_id):
        """
        Ajoute un personnage existant à une quête existante.
        Cela remplit automatiquement la table d'association personnage_quete.
        """
        quete = self.session.query(QueteModel).filter_by(id=quete_id).first()
        if not quete:
            print(f"❌ Quête ID {quete_id} introuvable.")
            return

        perso = self.session.query(Personnage).filter_by(id=personnage_id).first()
        if not perso:
            print(f"❌ Personnage ID {personnage_id} introuvable.")
            return

        if perso in quete.participants:
            print(f"⚠️ {perso.nom} participe déjà à cette quête.")
            return

        quete.participants.append(perso)
        self.commit()
        print(f"✅ {perso.nom} ajouté à la quête '{quete.titre}'.")
