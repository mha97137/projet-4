from tinydb import TinyDB, Query

class Player:
    def __init__(self, nom, prenom, naissance, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.sexe = sexe
        self.classement = classement
