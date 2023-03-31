class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("Age :", self.age)
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiere_enseignee):
        super().__init__()
        self.matiere_enseignee = matiere_enseignee
    
    def enseigner(self):
        print("Le cours va commencer")


personne = Personne()
eleve = Eleve()
professeur = Professeur("français")

personne.bonjour()  # Output : Hello

eleve.affichageAge()  # Output : J'ai 14 ans

eleve.allerEnCours()  # Output : Je vais en cours

professeur.enseigner()  # Output : Le cours va commencer