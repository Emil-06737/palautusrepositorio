class Summa:
    def __init__(self, sovelluslogiikka, syotteenlukufunktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.syotteenlukufunktio = syotteenlukufunktio
        self.edellinen_arvo = None

    def suorita(self):
        try:
            syote = int(self.syotteenlukufunktio())
        except ValueError:
            return
        self.edellinen_arvo = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.plus(syote)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Erotus:
    def __init__(self, sovelluslogiikka, syotteenlukufunktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.syotteenlukufunktio = syotteenlukufunktio
        self.edellinen_arvo = None

    def suorita(self):
        try:
            syote = int(self.syotteenlukufunktio())
        except ValueError:
            return
        self.edellinen_arvo = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.miinus(syote)

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Nollaus:
    def __init__(self, sovelluslogiikka, syotteenlukufunktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.syotteenlukufunktio = syotteenlukufunktio
        self.edellinen_arvo = None

    def suorita(self):
        self.edellinen_arvo = self.sovelluslogiikka.arvo()
        self.sovelluslogiikka.nollaa()

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_arvo)

class Kumoa:
    def __init__(self, komento):
        self.komento = komento

    def suorita(self):
        self.komento.kumoa()
