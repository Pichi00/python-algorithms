import math
import random


def is_in_pq(x, pq):
    for i in pq:
        if x == i[0]:
            return True
    return False


def prim(macierz):
    pred = [0] * len(macierz)
    k = [math.inf] * len(macierz)
    pq = list()
    s = random.randrange(len(macierz))
    k[s]=0
    for i in range(len(macierz)):
        pq.append([i, k[i]])
    # print(pq)
    # print("Pred: " + str(pred))
    # print("K: " + str(k))
    while(len(pq)>0):
        min = pq[0][1]
        min_index = 0
        for i in range(len(pq)):
            if pq[i][1] < min:
                min = pq[i][1]
                min_index = i
        u = pq.pop(min_index)
        # print("u[0] = "+str(u[0]))
        # print("macierz[u[0]] = "+str(macierz[u[0]]))
        v = 0
        for e in macierz[u[0]]:
            if e != 0 and is_in_pq(v, pq):
                waga = e
                # print("Waga: "+str(waga))
                # print("k: "+str(k[v]))
                if waga < k[v]:
                    pred[v] = u[0]
                    k[v] = waga
                    for i in pq:
                        if i[0]==v:
                            i[1]=k[v]
            v+=1
        # print("Pred: " + str(pred))
        # print("K: " + str(k))
        # print("pq: " + str(pq))

    print("Pred: "+str(pred))
    print("K: "+str(k))


graph1 = [
    [0,3,0,3,5], #0
    [3,0,5,1,0], #1
    [0,5,0,2,0], #2
    [3,1,2,0,1], #3
    [5,0,0,1,0], #4
]


prim(graph1)
