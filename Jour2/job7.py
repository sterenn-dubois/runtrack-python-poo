import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    couleurs = ["Pique", "Coeur", "Carreau", "Trèfle"]
    valeurs = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 10, "Dame": 10, "Roi": 10, "As": 11}
    
    def __init__(self):
        self.paquet = []
        self.creer_paquet()
        
    def creer_paquet(self):
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.paquet.append(Carte(valeur, couleur))
    
    def melanger(self):
        random.shuffle(self.paquet)
        
    def distribuer(self):
        return (self.paquet.pop(), self.paquet.pop())
    
    def ajouter_carte(self, carte):
        self.paquet.append(carte)
    
    def valeur_main(self, main):
        total = sum(self.valeurs[carte.valeur] for carte in main)
        nb_as = sum(carte.valeur == "As" for carte in main)
        while nb_as > 0 and total > 21:
            total -= 10
            nb_as -= 1
        return total
        

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        self.total = 0
        
    def ajouter_carte(self, carte):
        self.main.append(carte)
        self.total = self.calculer_total()
        
    def calculer_total(self):
        return sum(Jeu.valeurs[carte.valeur] for carte in self.main)
    
    def montrer_main(self, montree=True):
        if montree:
            print(f"{self.nom} a dans sa main : {', '.join(str(carte) for carte in self.main)}")
        else:
            print(f"{self.nom} a une carte cachée et {len(self.main) - 1} carte(s) : {', '.join(str(carte) for carte in self.main[1:])}")
    

class Blackjack:
    def __init__(self, nb_joueurs):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueurs = [Joueur("Joueur " + str(i+1)) for i in range(nb_joueurs)]
        self.croupier = Joueur("Croupier")
        
    def nouvelle_partie(self):
        for joueur in self.joueurs + [self.croupier]:
            joueur.main = []
            joueur.total = 0
            
        for i in range(2):
            for joueur in self.joueurs + [self.croupier]:
                carte = self.jeu.paquet.pop()
                joueur.ajouter_carte(carte)
                
        self.croupier.montrer_main(montree=False)
        for joueur in self.joueurs:
            joueur.montrer_main()
        
        for joueur in self.joueurs:
            self.jouer(joueur)
        
        self.croupier.montrer_main