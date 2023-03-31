class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
        
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

rectangle = Rectangle(5, 10)

print("Le périmètre du rectangle est:", rectangle.perimetre())
print("La surface du rectangle est:", rectangle.surface())
rectangle.set_longueur(7)
rectangle.set_largeur(12)
print("Le périmètre du rectangle est maintenant:", rectangle.perimetre())
print("La surface du rectangle est maintenant:", rectangle.surface())

parallelepipede = Parallelepipede(5, 10, 3)

print("Le volume du parallélépipède est:", parallelepipede.volume())
parallelepipede.set_longueur(7)
parallelepipede.set_largeur(12)
parallelepipede.set_hauteur(5)
print("Le volume du parallélépipède est maintenant:", parallelepipede.volume())