import time


def quick_sort(tab):
    left = list()
    equal = list()
    right = list()
    if len(tab) > 1:
        pivot = tab[0]
        for x in tab:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                right.append(x)
        return quick_sort(left)+equal+quick_sort(right)
    else:
        return tab


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
quick_sort(smallList) #Small list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")

#smallList = quick_sort(smallList)
#print(smallList) #Small list print

start = time.perf_counter()
quick_sort(mediumList) #Medium list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")

start = time.perf_counter()
quick_sort(largeList) #Large list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")
