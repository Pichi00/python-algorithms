import math

INF = math.inf

def floyd_warshall(d, p):
    n = len(d)
    for u in range(n):
        for v in range(n):
            if v != u:
                for w in range(n):
                    if w != u and w != v:
                        l = d[v][u] + d[u][w]
                        if l < d[v][w]:
                            d[v][w] = l
                            p[v][w] = p[u][w]
                        else:
                            d[v][w] = d[v][w]
                            p[v][w] = p[v][w]
    print("Macierz d:")
    for i in d:
        print(i)
    print("")
    print("Macierz p:")
    for i in p:
        print(i)
    print("")



macierz_d_1 = [
    [0,   3,   INF, INF, 3,   INF],  #Połączenia węzła 0
    [INF, 0,   1,   INF, INF, INF],  #Połączenia węzła 1
    [INF, INF, 0,   3,   INF, 1],    #Połączenia węzła 2
    [INF, 3,   INF, 0,   INF, INF],  #Połączenia węzła 3
    [INF, INF, INF, INF, 0,   2],    #Połączenia węzła 4
    [6,   INF, INF, 1,   INF, 0],    #Połączenia węzła 5
]

macierz_p_1 = [
    [0, 1, 0, 0, 1, 0],  # Połączenia węzła 0
    [0, 0, 2, 0, 0, 0],  # Połączenia węzła 1
    [0, 0, 0, 3, 0, 3],  # Połączenia węzła 2
    [0, 4, 0, 0, 0, 0],  # Połączenia węzła 3
    [0, 0, 0, 0, 0, 5],  # Połączenia węzła 4
    [6, 0, 0, 6, 0, 0],  # Połączenia węzła 5
]

macierz_d = [
    [0,   1,   5,   INF, INF, INF, INF],
    [INF, 0,   2,   INF, INF, INF, INF],
    [INF, INF, 0,   INF, INF, INF, INF],
    [7,   INF, INF, 0,   1,   INF, INF],
    [INF, INF, INF, INF, 0,   1,   INF],
    [2,   INF, INF, 4,   INF, 0,   INF],
    [6,   INF, INF, INF, INF, 3,   0]
]

macierz_p = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 5, 0],
    [6, 0, 0, 6, 0, 0, 0],
    [7, 0, 0, 0, 0, 7, 0]
]

floyd_warshall(macierz_d, macierz_p)
floyd_warshall(macierz_d_1, macierz_p_1)