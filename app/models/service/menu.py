import os
from models.service.race import Race
from models.service.personnage import Personnage
from models.service.anneau import Anneau
from models.service.quete import Quete
from models.db.quete import Quete as QueteModel  # pour lister les quêtes avec ID

class Menu:
    def __init__(self, session):
        self.session = session
        self.race = Race(session)
        self.personnage = Personnage(session)
        self.anneau = Anneau(session)
        self.quete = Quete(session)

        self.race.peupler()
        self.quete.peupler()

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("\n⏎ Appuyez sur Entrée pour continuer...")

    def affichage(self):
        while True:
            self.clear_console()
            print("\n🎮 Menu principal")
            print("1. Races")
            print("2. Personnages")
            print("3. Anneaux")
            print("4. Quêtes")
            print("0. Quitter")

            choix = input("Choix : ")
            if choix == "1":
                self.menu_race()
            elif choix == "2":
                self.menu_personnage()
            elif choix == "3":
                self.menu_anneau()
            elif choix == "4":
                self.menu_quete()
            elif choix == "0":
                break
            else:
                print("❌ Choix invalide.")
                self.pause()



    def menu_race(self):
        self.clear_console()
        print("\n🧬 RACES")
        print("1. Peupler")
        print("2. Lister")
        print("0. Retour")
        choix = input("Choix : ")

        if choix == "1":
            self.race.peupler()
            self.pause()

        elif choix == "2":
            print("\n📜 Races disponibles :")
            for r in self.race.lister():
                print(f"[{r.id}] {r.nom}")
            self.pause()

    def menu_personnage(self):
        self.clear_console()
        print("\n🧙 PERSONNAGES")
        print("1. Ajouter")
        print("2. Lister")
        print("3. Chercher par nom")
        print("4. Chercher par ID")
        print("5. Modifier nom")
        print("6. Supprimer")
        print("7. Avec quêtes")
        print("8. Ayant un anneau")
        print("0. Retour")
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom : ")

            print("\n📜 Liste des races disponibles :")
            for r in self.race.lister():
                print(f"[{r.id}] {r.nom}")

            try:
                race_id = int(input("ID de la race : "))
                from models.db.race import Race as RaceModel
                race = self.session.query(RaceModel).filter_by(id=race_id).first()
                if not race:
                    print("❌ Race introuvable.")
                else:
                    self.personnage.ajouter(nom, race)
                    print(f"✅ Personnage '{nom}' ajouté avec la race '{race.nom}'.")
            except ValueError:
                print("❌ Entrée invalide.")

            self.pause()

        elif choix == "2":
            for p in self.personnage.lister():
                self.personnage.afficher_details(p)
            self.pause()

        elif choix == "3":
            nom = input("Nom (partiel) : ")
            results = self.personnage.chercher_par_nom(nom)
            for p in results:
                print(f"- {p.nom}")
            self.pause()

        elif choix == "4":
            id_ = int(input("ID : "))
            p = self.personnage.chercher_par_id(id_)
            if p:
                self.personnage.afficher_details(p)
            self.pause()

        elif choix == "5":
            id_ = int(input("ID : "))
            nouveau_nom = input("Nouveau nom : ")
            self.personnage.modifier(id_, nouveau_nom)
            self.pause()

        elif choix == "6":
            id_ = int(input("ID à supprimer : "))
            self.personnage.supprimer(id_)
            self.pause()

        elif choix == "7":
            for p in self.personnage.avec_quetes():
                print(f"{p.nom}")
            self.pause()

        elif choix == "8":
            for p in self.personnage.ayant_anneau():
                print(f"{p.nom}")
            self.pause()

    def menu_anneau(self):
        self.clear_console()
        print("\n💍 ANNEAUX")
        print("1. Ajouter")
        print("2. Lister")
        print("3. Chercher par nom")
        print("4. Supprimer par ID")
        print("0. Retour")
        choix = input("Choix : ")

        if choix == "1":
            nom = input("Nom de l'anneau : ")
            pid = input("ID du porteur (laisser vide si aucun) : ")
            pid = int(pid) if pid.strip() != "" else None
            self.anneau.ajouter(nom, pid)
            self.pause()

        elif choix == "2":
            self.anneau.lister()
            self.pause()

        elif choix == "3":
            nom = input("Nom : ")
            result = self.anneau.chercher_par_nom(nom)
            print(result)
            self.pause()

        elif choix == "4":
            id_ = int(input("ID : "))
            self.anneau.supprimer_par_id(id_)
            self.pause()

    def menu_quete(self):
        self.clear_console()
        print("\n📜 QUÊTES")
        print("1. Associer un personnage à une quête")
        print("0. Retour")
        choix = input("Choix : ")

        if choix == "1":
            try:
                print("\n👤 Personnages disponibles :")
                for p in self.personnage.lister():
                    print(f"[{p.id}] {p.nom}")

                print("\n🗺️ Quêtes disponibles :")
                for q in self.quete.session.query(QueteModel).all():
                    print(f"[{q.id}] {q.titre}")

                pid = int(input("\nID personnage : "))
                qid = int(input("ID quête : "))
                self.quete.ajouter_personnage(qid, pid)

            except ValueError:
                print("❌ ID invalide.")
            self.pause()
