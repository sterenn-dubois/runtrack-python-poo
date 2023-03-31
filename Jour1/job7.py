class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

livre = Livre("Daily Stoic", "Ryan Holiday", 365)
print("Titre du livre:", livre.get_titre())
print("Auteur du livre:", livre.get_auteur())
print("Nombre de pages du livre:", livre.get_nb_pages())

livre.set_titre("The 48 Law Of Power")
livre.set_auteur("Robert Green")
livre.set_nb_pages(367)
print("Nouveau titre du livre:", livre.get_titre())
print("Nouvel auteur du livre:", livre.get_auteur())
print("Nouveau nombre de pages du livre:", livre.get_nb_pages())

livre.set_nb_pages(-100) 
print("Nombre de pages du livre après une tentative de modification invalide:", livre.get_nb_pages())