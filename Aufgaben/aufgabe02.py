import random


def lottoziehung(anzahl_zahlen=6):
    kugeln = list(range(1, 46))
    letzter = 44

    for i in range(anzahl_zahlen):
        index = random.randint(0, letzter)
        kugeln[index], kugeln[letzter] = kugeln[letzter], kugeln[index]
        letzter -= 1

    return kugeln[letzter + 1:]


def statistik_aktualisieren(statistik, ziehung):
    for zahl in ziehung:
        statistik[zahl] += 1


def lotto_statistik(anzahl):
    statistik = {}
    for zahl in range(1, 46):
        statistik[zahl] = 0

    for i in range(anzahl):
        ziehung = lottoziehung()
        statistik_aktualisieren(statistik, ziehung)

    return statistik


def statistik_ausgeben(statistik, anzahl):
    print("\nStatistik nach", anzahl, "Ziehungen:")
    for zahl in statistik:
        prozent = statistik[zahl] / (anzahl * 6) * 100
        print(zahl, ":", statistik[zahl], "-", round(prozent, 2), "%")

# print("Lottozahlen:", sorted(lottoziehung()))

# alle = lottoziehung(45)
# print("Alle 45 gezogen, keine doppelt:", sorted(alle) == list(range(1, 46)))

for anzahl in [1000, 10000, 100000]:
    statistik = lotto_statistik(anzahl)
    statistik_ausgeben(statistik, anzahl)