from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Pelitehdas:
    @staticmethod
    def pelivaihtoehdot():
        return ("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan")

    @staticmethod
    def luo_peli(tyyppi):
        tyypit = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }

        if tyyppi in tyypit:
            return tyypit[tyyppi]
        return None
