class Personne:
    
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("J'ai", self.age, "ans.")
    
    def bonjour(self):
        print("Hello!")

    def modifierAge(self, nouvelAge):
        self.age = nouvelAge

class Eleve(Personne):
    
    def __init__(self):
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours.")
    
    def afficherAge(self):
        print("J'ai", self.age, "ans.")

class Professeur(Personne):
    
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer.")

eleve = Eleve()

eleve.bonjour()
eleve.allerEnCours()

eleve.modifierAge(15)

eleve.afficherAge()

professeur = Professeur(40, "français")

professeur.bonjour()
professeur.enseigner()





