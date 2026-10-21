import random

def getLottoZahlen(anz, ziehen):

    zahlen = list(range(1, anz+1))
    letzter = anz-1

    for _ in range(ziehen):
        randNumber = random.randint(0, letzter)

        zahlen[randNumber], zahlen[letzter] = zahlen[letzter], zahlen[randNumber]
        letzter -= 1

    return zahlen[letzter+1:]

def ausgeben(x, statistic):
    print(statistic)

def statistikAktu(statistic, nums):
    for x in nums:
        statistic[x] += 1

def lottoStatistik(anz, ziehen, x):
    statistic = {}

    for y in range(1, anz+1):
        statistic[y] = 0

    for i in range(0, x):
        nums = getLottoZahlen(anz, ziehen);
        statistikAktu(statistic, nums)

    return statistic

#x = int(input("Wieviele Zahlen soll man ziehen?"))
#y = getLottoZahlen(45,6)
#print("Lottozahlen: ", y)


for x in [100, 1000, 10000]:
    stat = lottoStatistik(45, 6, x)
    ausgeben(x, stat);



#for i in range(1, 11):
 #   print(f"Die quadrierte Zahl von {i} ist {i*i}")

