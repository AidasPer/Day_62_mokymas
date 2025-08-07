

class Kursas:
    def __init__(self, pavadinimas, destytojas, trukme):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = trukme

    def destyti(self):
        print("Vyksta mokymas!")

    def __repr__(self):
        return f"Pamoka: {self.pavadinimas}, Destytojas: {self.destytojas}, Trukme(val): {self.trukme}"