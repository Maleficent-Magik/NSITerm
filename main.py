import datetime


class Date:

    def __init__(self, jour, mois, annee):
        if 1 <= jour <= 31:
            self.jour = jour
        else:
            raise ValueError("Attention ! Le jour doit compter entre 1 et 31 jours !")

        if 1 <= mois <= 12:
            self.mois = mois
        else:
            raise ValueError("Attention ! Le mois doit être entre 1 et 12 !")

        if 0 <= annee:
            self.annee = annee
        else:
            raise ValueError("Attention ! L'année doit être compris positif.")

    def get_jourSemaine(self)-> str:
        JS = ['Lundi', 'Mardi', 'Mercerdi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        pass

    def estBissxetile(self):


    def __str__(self):
        mois = ['Lundi', 'Mardi', 'Mercerdi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        return (self.jour, Date.JS[self.mois-1], self.annee)

    def __lt__(self, d):
        if self.annee < d.annee:
            return True
        elif self.annee > d.annee:
            return False
        else:
            if self.mois < d.mois:
                return True
            elif self.mois > d.mois:
                return False
            else:
                return self.jour < d.jour

d1 = Date(30, 3, 2020)
d2 = Date(11, 3, 2020)
print(d1 < d2)
