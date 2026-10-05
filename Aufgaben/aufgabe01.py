"""
Bankomat-Simulation – Übungsbeispiel für Python-Kontrollstrukturen
Themen: if/elif/else, for, while, break, continue, pass,
        try-except-else-finally

Test-PIN: 1234
"""

RICHTIGE_PIN = "1234"
kontostand = 500.0


def kontoauszug_drucken():
    pass  # PASS: Funktion ist noch nicht implementiert


# ---------- 1. PIN-Eingabe: FOR + BREAK (max. 3 Versuche) ----------
angemeldet = False
for versuch in range(1, 4):
    pin = input(f"PIN eingeben (Versuch {versuch}/3): ")
    if pin == RICHTIGE_PIN:
        angemeldet = True
        break  # richtige PIN -> keine weiteren Versuche nötig
    print("  Falsche PIN!")

if not angemeldet:
    print("Karte wurde eingezogen. Bitte wenden Sie sich an Ihre Bank.")
    exit()

# ---------- 2. Hauptmenü: WHILE-Schleife ----------
while True:
    print("\n1 = Kontostand | 2 = Abheben | 3 = Kontoauszug | 4 = Beenden")
    auswahl = input("Auswahl: ")

    # IF / ELIF / ELSE: Menüauswahl auswerten
    if auswahl == "1":
        print(f"Kontostand: {kontostand:.2f} €")

    elif auswahl == "2":
        # TRY-EXCEPT-ELSE-FINALLY: ungültige Beträge abfangen
        try:
            betrag = float(input("Betrag in €: "))
        except ValueError:
            # läuft nur, wenn ein Fehler auftritt
            print("  Fehler: Bitte eine Zahl eingeben!")
            continue  # zurück zum Menü (finally läuft trotzdem!)
        else:
            # läuft nur, wenn KEIN Fehler aufgetreten ist
            if betrag <= 0:
                print("  Fehler: Betrag muss positiv sein!")
            elif betrag % 10 != 0:
                print("  Fehler: Nur 10-€-Schritte möglich!")
            elif betrag > kontostand:
                print("  Fehler: Kontostand nicht ausreichend!")
            else:
                kontostand -= betrag
                print(f"  {betrag:.2f} € ausgezahlt. Neuer Stand: {kontostand:.2f} €")
        finally:
            # läuft IMMER – mit oder ohne Fehler
            print("  Abhebevorgang beendet.")

    elif auswahl == "3":
        kontoauszug_drucken()
        print("  Diese Funktion ist bald verfügbar.")

    elif auswahl == "4":
        print("Auf Wiedersehen!")
        break  # verlässt das Hauptmenü

    else:
        print("  Ungültige Auswahl!")