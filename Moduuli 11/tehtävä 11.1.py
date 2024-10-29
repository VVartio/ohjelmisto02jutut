class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulostus(self):
        print(f"Julkaisun nimi: {self.nimi}")
        return

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivunumero):
        self.kirjoittaja = kirjoittaja
        self.sivunumero = sivunumero
        super().__init__(nimi)
    def tulostus(self):
        super().tulostus()
        print(f"Kirjan kirjoittaja ja sivunumero: {self.kirjoittaja, self.sivunumero}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)
    def tulostus(self):
        super().tulostus()
        print(f"Lehden päätoimittaja: {self.päätoimittaja}")

julkaisut = []

julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))

for i in julkaisut:
    i.tulostus()