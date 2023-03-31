class Animal:
    def __init__(self):
        self.age = 9
        self.nom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.nom = nom

animal = Animal()
print("Age de l'animal:", animal.age)

animal.vieillir()
print("Age de l'animal après avoir vieilli:", animal.age)

animal.nommer("Gacy")
print("Nom de l'animal:", animal.nom)

