import random


def lottoziehung():
    kugeln = list(range(1, 46))   # [1, 2, ..., 45]
    gezogen = []
    letzter = 44                  # letzter freier Index

    for i in range(6):
        index = random.randint(0, letzter)          # 1 Zufallsaufruf pro Zahl
        gezogen.append(kugeln[index])
        kugeln[index] = kugeln[letzter]             # letzte freie Kugel ins Loch
        letzter -= 1                                # Bereich wird kleiner

    return gezogen


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


print("Lottozahlen:", sorted(lottoziehung()))

for anzahl in [1000, 10000, 100000]:
    print("\nStatistik nach", anzahl, "Ziehungen:")
    statistik = lotto_statistik(anzahl)
    for zahl in statistik:
        print(zahl, ":", statistik[zahl])