import time


def merge_sort(tab):
    if len(tab) > 1:
        mid = len(tab)//2
        q1 = tab[:mid]
        q2 = tab[mid:]
        merge_sort(q1)
        merge_sort(q2)
        i = 0
        j = 0
        k = 0
        while i < len(q1) and j < len(q2):
            if q1[i] < q2[j]:
                tab[k] = q1[i]
                i += 1
            else:
                tab[k] = q2[j]
                j += 1
            k += 1
        while i < len(q1):
            tab[k] = q1[i]
            i += 1
            k += 1
        while j < len(q2):
            tab[k] = q2[j]
            j += 1
            k += 1


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
merge_sort(smallList) #Small list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")
#git print(smallList) #Small list print

start = time.perf_counter()
merge_sort(mediumList) #Medium list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")

start = time.perf_counter()
merge_sort(largeList) #Large list sort
end = time.perf_counter()
print("Duration of the operation: " + str(end - start) + " s")
