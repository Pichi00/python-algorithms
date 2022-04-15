import time


def insertion_sort(tab):
    start = time.perf_counter()
    for i in range(1, len(tab)):
        tmp = tab[i]
        j = i - 1
        while j >= 0 and tmp < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = tmp
    end = time.perf_counter()
    print("Duration of the operation: " + str(end-start) + " s")


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


insertion_sort(smallList) #Small list sort
print(smallList) #Check if list is sorted
insertion_sort(mediumList) #Medium list sort
#print(mediumList) #Check if list is sorted
#insertion_sort(largeList) #Large list sort
#print(largeList) #Check if list is sorted