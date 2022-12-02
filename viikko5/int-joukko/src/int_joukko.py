class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.__taulukko = [0] * self.kapasiteetti
        self.__alkioiden_lkm = 0

    def kuuluu(self, luku):
        if self._hae_sijainti(luku) < 0:
            return False
        return True

    def lisaa(self, lisattava):
        if self.__alkioiden_lkm == 0:
            self.__taulukko[0] = lisattava
            self.__alkioiden_lkm += 1
            return True

        if self.kuuluu(lisattava):
            return False

        if self.__alkioiden_lkm >= len(self.__taulukko):
            self._luo_uusi_taulukko()
        self.__taulukko[self.__alkioiden_lkm] = lisattava
        self.__alkioiden_lkm += 1
        return True

    def _luo_uusi_taulukko(self):
        uusi_taulukko = [0] * (self.__alkioiden_lkm + self.kasvatuskoko)
        self._kopioi_taulukon_sisalto(self.__taulukko, uusi_taulukko)
        self.__taulukko = uusi_taulukko

    def poista(self, luku):
        kohta = self._hae_sijainti(luku)
        if kohta < 0:
            return False
        self._siirra_lukuja_vasemmalle(kohta)
        self.__alkioiden_lkm = self.__alkioiden_lkm - 1
        return True

    def _hae_sijainti(self, luku):
        for i in range(0, self.__alkioiden_lkm):
            if luku == self.__taulukko[i]:
                return i
        return -1

    def _siirra_lukuja_vasemmalle(self, aloituskohta):
        for i in range(aloituskohta, self.__alkioiden_lkm - 1):
            self.__taulukko[i] = self.__taulukko[i + 1]

    def _kopioi_taulukon_sisalto(self, vanha_taulukko, uusi_taulukko):
        for i in range(0, len(vanha_taulukko)):
            uusi_taulukko[i] = vanha_taulukko[i]

    def mahtavuus(self):
        return self.__alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.__alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.__taulukko[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            yhdistejoukko.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            yhdistejoukko.lisaa(b_taulu[i])
        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            if b.kuuluu(a_taulu[i]):
                leikkausjoukko.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            if a.kuuluu(b_taulu[i]):
                leikkausjoukko.lisaa(b_taulu[i])
        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            erotusjoukko.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            erotusjoukko.poista(b_taulu[i])
        return erotusjoukko

    def __str__(self):
        mjono = "{"
        for i in range(0, self.__alkioiden_lkm):
            mjono += str(self.__taulukko[i])
            if i < self.__alkioiden_lkm - 1:
                mjono += ", "
        mjono += "}"
        return mjono
