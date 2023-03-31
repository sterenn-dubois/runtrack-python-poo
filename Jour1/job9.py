class Student:
    def __init__(self, nom, prenom, identifiant):
        self.nom = nom
        self.prenom = prenom
        self.identifiant = identifiant
        self.credits = 0
        self.level = self.__studentEval()
    
    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits
    
    def __studentEval(self):
        if self.credits >= 90:
            return "Excellent"
        elif self.credits >= 80:
            return "Très bien"
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print(f"nom = {self.nom}, prenom = {self.prenom}, id = {self.identifiant}, niveau = {self.level}")

john_doe = Student("Doe", "Jon", 145)

john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

john_doe.studentInfo()