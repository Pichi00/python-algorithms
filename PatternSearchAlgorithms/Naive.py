#Texts and patterns
text1 = "Patter search"
pattern1 = "ear"
text2 = "ADABACA"
text3 = "CSFBADXBCABDZABDABC"
pattern2 = "ADA"
pattern3 = "ACA"
pattern4 = "ABDABC"
pattern5 = "DADADA"


def naive(T, x):
    match = False
    pos = 0
    for i in range(len(T) - len(x)+1):
        if T[i] == x[0]:
            for j in range(len(x)):
                if T[i+j] != x[j]:
                    match = False
                    break
                match = True
        if match:
            pos = i
            break
    if match:
        print("Pattern found at position "+str(pos))
    else:
        print("Pattern not found")


#Tests
naive(text1, pattern1)
naive(text2, pattern2)
naive(text2, pattern3)
naive(text2, pattern4)
naive(text2, pattern5)
naive(text3, pattern4)
