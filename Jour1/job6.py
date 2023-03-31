class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle = Rectangle(10, 5)
print("Longueur du rectangle:", rectangle.get_longueur())
print("Largeur du rectangle:", rectangle.get_largeur())

rectangle.set_longueur(12)
rectangle.set_largeur(6)
print("Nouvelle longueur du rectangle:", rectangle.get_longueur())
print("Nouvelle largeur du rectangle:", rectangle.get_largeur())