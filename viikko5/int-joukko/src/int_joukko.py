KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.tarkista_kapasiteetti(kapasiteetti)
        self.tarkista_kasvatuskoko(kasvatuskoko)
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_Lkm = 0

    def kuuluu(self, luku):
        return luku in self.lista

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lista[self.alkioiden_Lkm] = luku
            self.alkioiden_Lkm = self.alkioiden_Lkm + 1

            if self.lista_on_taynna():
                self.kopioi_lista_isompaan_listaan()

            return True
        
        return False

    def poista(self, luku):
        if not self.kuuluu(luku):
            return False
        poistettavan_indeksi = self.lista.index(luku)
        self.paivita_lista_poiston_mukaiseksi(poistettavan_indeksi)
        self.alkioiden_Lkm = self.alkioiden_Lkm - 1
        return True

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_Lkm

    def to_int_list(self):
        oikean_pituinen_lista = self._luo_lista(self.alkioiden_Lkm)

        for i in range(self.alkioiden_Lkm):
            oikean_pituinen_lista[i] = self.lista[i]

        return oikean_pituinen_lista

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_luku in a_taulu:
            yhdiste.lisaa(a_luku)

        for b_luku in b_taulu:
            yhdiste.lisaa(b_luku)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_luku in a_taulu:
            if a_luku in b_taulu:
                leikkaus.lisaa(a_luku)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_luku in a_taulu:
            erotus.lisaa(a_luku)

        for b_luku in b_taulu:
            erotus.poista(b_luku)

        return erotus

    def __str__(self):
        keskiosa = ""
        for i in range(self.alkioiden_Lkm):
            keskiosa = keskiosa + str(self.lista[i]) + ", "
        keskiosa = keskiosa[:-2]

        return f"{{{keskiosa}}}"

    def tarkista_kapasiteetti(self, kapasiteetti):
        if not isinstance(kapasiteetti, int):
            raise TypeError("Kapasiteetin täytyy olla kokonaisluku!")
        elif kapasiteetti < 0:
            raise ValueError("Kapasiteetin täytyy olla vähintään nolla!")

    def tarkista_kasvatuskoko(self, kasvatuskoko):
        if not isinstance(kasvatuskoko, int):
            raise TypeError("Kasvatuskoon täytyy olla kokonaisluku!")
        elif kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon täytyy olla vähintään nolla!")

    def lista_on_taynna(self):
        return self.alkioiden_Lkm % len(self.lista) == 0
    
    def kopioi_lista_isompaan_listaan(self):
        vanha_lista = self.lista
        self.kopioi_lista(self.lista, vanha_lista)
        self.lista = self._luo_lista(self.alkioiden_Lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista, self.lista)

    def paivita_lista_poiston_mukaiseksi(self, poistettavan_indeksi):
        for i in range(poistettavan_indeksi, self.alkioiden_Lkm - 1):
            self.lista[i] = self.lista[i + 1]
        self.lista[self.alkioiden_Lkm - 1] = 0
