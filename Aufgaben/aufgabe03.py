# HÜ: je eine list, set und dict comprehension mit if else

zahlen = list(range(1, 11))

# List Comprehension: gerade Zahlen quadrieren, ungerade negieren
liste = [x ** 2 if x % 2 == 0 else -x for x in zahlen]

# Set Comprehension: jede Zahl als "gerade" oder "ungerade" einordnen
woerter = {"gerade" if x % 2 == 0 else "ungerade" for x in zahlen}

# Dict Comprehension: Zahl -> "Fizz" wenn durch 3 teilbar, sonst die Zahl selbst
fizz = {x: "Fizz" if x % 3 == 0 else x for x in zahlen}


if __name__ == "__main__":
    print("List:", liste)
    print("Set: ", woerter)
    print("Dict:", fizz)
