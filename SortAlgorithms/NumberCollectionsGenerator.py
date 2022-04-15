import random
#Generates file with small collection of random numbers (100)
f1 = open("data/smallCollection.txt", "w")
for i in range(100):
    f1.write(str(random.randint(-500, 500))+'\n')
f1.close()

#Generates file with madium collection of random numbers (10000)
f2 = open("data/mediumCollection.txt", "w")
for i in range(10000):
    f2.write(str(random.randint(-500, 500))+'\n')
f2.close()

#Generates file with large collection of random numbers (1000000)
f3 = open("data/largeCollection.txt", "w")
for i in range(100000):
    f3.write(str(random.randint(-500, 500))+'\n')
f3.close()