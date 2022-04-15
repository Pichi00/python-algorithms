import time


def bubble_sort(tab):
    start = time.perf_counter()
    n = len(tab)
    for i in range(n-1):
        for j in range(n-1-i):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    end = time.perf_counter()
    print("Duration of the operation: " + str(end - start) + " s")


#tests
smallList = list()
mediumList = list()
#largeList = list()

f1 = open("data/smallCollection.txt", "r")
for line in f1:
    smallList.append(int(line))
f1.close()

f2 = open("data/mediumCollection.txt", "r")
for line in f2:
    mediumList.append(int(line))
f2.close()

#f3 = open("data/largeCollection.txt", "r")
#for line in f3:
#    largeList.append(int(line))
#f3.close()


bubble_sort(smallList) #Small list sort
print(smallList) #Check if list is sorted
bubble_sort(mediumList) #Medium list sort
#print(mediumList) #Check if list is sorted
#bubble_sort(largeList) #Large list sort #Takes over 20 minutes
#print(largeList) #Check if list is sorted