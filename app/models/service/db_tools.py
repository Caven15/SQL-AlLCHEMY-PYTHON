class DBTools:
    def __init__(self, session):
        self.session = session

    def commit(self):
        """
        Valide la transaction. Si une erreur survient, elle effectue un rollback
        puis relance l'exception pour traitement ou affichage.
        """
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()