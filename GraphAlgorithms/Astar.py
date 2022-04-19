import math

def is_in_list(x, q):
    for i in q:
        if x == i:
            return True
    return False

def astar(macierz, h):
    n = len(macierz)
    pred = [-1] * n
    g = [math.inf] * n
    f = [math.inf] * n
    #Zbiory wierzchołków
    Q = list()
    S = list()
    #Wybieramy wierzchołek startowy i ustawiamy jego drogę na 0
    s = 0
    g[s] = 0
    Q.append(s)

    while len(Q) > 0:
        u = Q[0]
        for i in Q:
            if g[i] < g[u]:
                u = i
        S.append(Q.pop(Q.index(u)))
        w = 0
        for e in macierz[u]:
            if e != 0:
                if is_in_list(w, Q):
                    if g[w] > g[u] + e:
                        g[w] = g[u] + e
                        f[w] = g[w] + h[w]
                        pred[w] = u
                if not is_in_list(w, Q) and not is_in_list(w, S):
                    Q.append(w)
                    g[w] = g[u] + e
                    f[w] = g[w] + h[w]
                    pred[w] = u
            w += 1
    print("h:       " + str(h))
    print("f:       " + str(f))
    print("g:       " + str(g))
    print("pred:    " + str(pred))


graf_skierowany = [
    [0, 3, 0, 0, 3, 0],  #Połączenia węzła 0
    [0, 0, 1, 0, 0, 0],  #Połączenia węzła 1
    [0, 0, 0, 3, 0, 1],  #Połączenia węzła 2
    [0, 3, 0, 0, 0, 0],  #Połączenia węzła 3
    [0, 0, 0, 0, 0, 2],  #Połączenia węzła 4
    [6, 0, 0, 1, 0, 0],  #Połączenia węzła 5
]

#Szacowane odległości do węzła 5
szacowaneOdleglosci = [2, 2, 1, 3, 1, 0]

#Przykład prezentujący znalezienie najkrótszej drogi z wierzchołka 0 do 5
astar(graf_skierowany, szacowaneOdleglosci)