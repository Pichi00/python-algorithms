import math
import random

def dijkstry(macierz):
    n = len(macierz)
    d = [math.inf] * n
    p = [-1] *  n
    #Zbiory wierzchołków
    Q = list(range(n))
    S = list()
    #Losujmy wierzchołek startowy i ustawiamy jego drogę na 0
    d[random.randrange(n)] = 0

    while len(Q) > 0:
        #Wybieramy indeks wierzchołka o najmniejszej wartości d
        u = Q[0]
        for i in Q:
            if d[i] < d[u]:
                u = i
        #Usuwamy wierzchołek u ze zbioru Q i dodajemy do zbioru S
        S.append(Q.pop(Q.index(u)))
        w = 0
        for i in macierz[u]:
            if i != 0:
                if d[w] > d[u] + i:
                    d[w] = d[u] + i
                    p[w] = u
            w += 1

    print("pred: " + str(p))
    print("dist: " + str(d))




#Graf skierowany:
#Połączenia: indeks_wiersza -> indeks_kolumny
#Np.: Węzeł o indeksie 0 wskazuje na węzeł o indeksie 1 z wagą 3.
graf_skierowany = [
    [0, 3, 0, 0, 3, 0], #Połączenia węzła 0
    [0, 0, 1, 0, 0, 0], #Połączenia węzła 1
    [0, 0, 0, 3, 0, 1], #Połączenia węzła 2
    [0, 3, 0, 0, 0, 0], #Połączenia węzła 3
    [0, 0, 0, 0, 0, 2], #Połączenia węzła 4
    [6, 0, 0, 1, 0, 0], #Połączenia węzła 5
]

dijkstry(graf_skierowany)