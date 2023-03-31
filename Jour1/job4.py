class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
p1 = Personne("Doe", "John")
p2 = Personne("Gacy", "John Wayne")

print(p1.SePresenter())
print(p2.SePresenter())