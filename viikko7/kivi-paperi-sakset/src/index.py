from pelitehdas import Pelitehdas


def main():
    while True:
        print(Pelitehdas().pelivaihtoehdot())

        vastaus = input()
        if vastaus:
            peli = Pelitehdas().luo_peli(vastaus[-1])
        else:
            break

        if peli:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
