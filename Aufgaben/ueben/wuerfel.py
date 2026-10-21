import random

def wuerfeln(anz, countSides):
    y = random.randint(1, countSides)
    return y

def initialSta(countSides):
    sta = {}
    for i in range(1,countSides+1):
        sta[i] = 0
    return sta

def wuerfeln_statistic(anz, countSides):
    statistic = initialSta(countSides)
    for x in range(anz):
        auge = wuerfeln(anz, countSides)
        statistic[auge] += 1
    return statistic


sta = wuerfeln_statistic(10000, 6)
print(sta)


noten = {}



