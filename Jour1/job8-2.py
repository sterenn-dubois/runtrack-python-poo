class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True

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

    def verification(self):
        if self.__disponible:
            print("Le livre est disponible.")
        else:
            print("Le livre n'est pas disponible.")

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print("Le livre a bien été emprunté.")
        else:
            print("Le livre n'est pas disponible.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print("Le livre a bien été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

livre1 = Livre("Il était deux fois", "Franck Thilliez", 597)
livre1.verification()  # Le livre est disponible.
livre1.emprunter()  # Le livre a bien été emprunté.
livre1.verification()  # Le livre n'est pas disponible.
livre1.rendre()  # Le livre a bien été rendu.
livre1.verification()  # Le livre est disponible.
livre1.rendre()  # Le livre n'a pas été emprunté.            