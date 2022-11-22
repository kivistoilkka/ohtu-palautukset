from functools import reduce
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return reduce(lambda summa, ostos: summa+ostos.lukumaara(), self._ostokset.values(), 0)

    def hinta(self):
        return reduce(lambda summa, ostos: summa+ostos.hinta(), self._ostokset.values(), 0)

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() not in self._ostokset:
            self._ostokset[lisattava.nimi()] = Ostos(lisattava)
            return
        self._ostokset[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        self._ostokset[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self._ostokset[poistettava.nimi()].lukumaara() == 0:
            del self._ostokset[poistettava.nimi()]

    def tyhjenna(self):
        self._ostokset.clear()

    def ostokset(self):
        return list(self._ostokset.values())
