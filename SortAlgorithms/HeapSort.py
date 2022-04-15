import math
import time


def heapify(tab, i, m):
    maks = m
    l = 2 * m + 1
    r = 2 * m + 2
    if l < i and tab[maks] < tab[l]:
        maks = l
    if r < i and tab[maks] < tab[r]:
        maks = r
    if maks != m:
        temp = tab[m]
        tab[m] = tab [maks]
        tab[maks] = temp
        heapify(tab, i, maks)


def heap_sort(tab):
    n = len(tab)
    for i in range(math.floor(n/2)-1, -1, -1):
        heapify(tab, n, i)
    for i in range(n-1, 0, -1):
        temp = tab[i]
        tab[i] = tab[0]
        tab[0] = temp
        heapify(tab, i, 0)


#tests
smallList = list()
mediumList = list()
largeList = list()

f1 = open("data/smallCollection.txt", "r")
for line in f1:
    smallList.append(int(line))
f1.close()

f2 = open("data/mediumCollection.txt", "r")
for line in f2:
    mediumList.append(int(line))
f2.close()

f3 = open("data/largeCollection.txt", "r")
for line in f3:
    largeList.append(int(line))
f3.close()


start = time.perf_counter()
heap_sort(smallList) #Small list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")
#print(smallList) #Small list print

start = time.perf_counter()
heap_sort(mediumList) #Medium list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")

start = time.perf_counter()
heap_sort(largeList) #Large list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")