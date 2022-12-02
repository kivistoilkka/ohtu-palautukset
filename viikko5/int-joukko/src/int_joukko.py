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
        self._kopioi_taulukko(self.__taulukko, uusi_taulukko)
        self.__taulukko = uusi_taulukko

    def poista(self, luku):
        kohta = self._hae_sijainti(luku)
        if kohta < 0:
            return False
        self.__taulukko[kohta] = 0
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

    def _kopioi_taulukko(self, vanha_taulukko, uusi_taulukko):
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
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.__alkioiden_lkm == 0:
            return "{}"
        elif self.__alkioiden_lkm == 1:
            return "{" + str(self.__taulukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.__alkioiden_lkm - 1):
                tuotos = tuotos + str(self.__taulukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.__taulukko[self.__alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
