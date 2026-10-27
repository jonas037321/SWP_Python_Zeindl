import random

#Pokerspielsimulator als Aufgabe über Herbstferien


def searchHand(colorsTaken, symbolsTaken):
    flush = False
    for c in colorsTaken:
        if c == 5:
            flush = True

    drill = 0
    pair = 0
    fourOAKind = 0

    street = 0

    for i in range(0,13):
        match symbolsTaken[i]:
            case 0: street = 0
            case 1:
                street += 1
                if street == 5:
                    if flush is True:
                        if i == 12:
                            return 6 # Royal Flush
                        else:
                            return 5 #Straight Flush
                    else:
                        return 4 #Straße

            case 2: pair += 1
            case 3: drill += 1
            case 4: fourOAKind +=1

    if flush is True:
        return 3
    if pair == 2:
        return 7
    if pair  == 1:
        if drill == 1:
            return 8
        else:
            return 0
    if drill == 1:
        return 1 # Drilling
    if fourOAKind == 1:
        return 2
    return 9


def getFiveRandom(anz):
    nums = list(range(anz))
    letzter = anz-1
    for _ in range(5):
        zahl = random.randint(0,letzter)
        nums[zahl], nums[letzter] = nums[letzter], nums[zahl]
        letzter -= 1

    return nums[letzter + 1:]

def statisticAktualisieren(zahlen):
    # 0.... Pair
    # 1... Drilling
    # 2 ... Four of a Kind
    # 3 ... Flush
    # 4 ... Straße
    # 5 ... Strait Flush
    # 6... Royal Flush
    # 7... two pair
    # 8 ... full house
    # 9 ... nix / high card
    colorsTaken = [0] * 4
    symbolsTaken = [0] * 13
    for z in zahlen:
        color = z // 13
        symb = z % 13

        colorsTaken[color] += 1
        symbolsTaken[symb] += 1

    x = searchHand(colorsTaken, symbolsTaken)
    return x


def statisticAusgeben(stat):
    for s in stat:
        print()


# x = getFiveRandom()
# print(x)

anz_Spiele = 1000000
statistik_anzahlen = [0] * 10
statistik = {
        9: "High Card",
        0: "Ein Paar",
        1: "Drilling",
        2: "Four of a Kind",
        3: "Flush",
        4: "Straße",
        5: "Straight Flush",
        6: "Royal Flush",
        7: "Two Pair",
        8: "Full House"
    }

for _ in range(anz_Spiele):
    zahlen = getFiveRandom(52)
    zahlen.sort()
    #print(zahlen)

    stat = statisticAktualisieren(zahlen)
    statistik_anzahlen[stat] += 1


for i in range(0, 10):
    x = statistik_anzahlen[i]
    percentage = x / anz_Spiele * 100
    print(statistik[i], " wurde so oft gezogen: ", x, " Das sind soviel Prozent: ", round(percentage, 2), "%")

