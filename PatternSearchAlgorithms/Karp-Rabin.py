#Texts and patterns
text1 = "Patter search"
pattern1 = "ear"
text2 = "ADABACA"
text3 = "CSFBADXBCABDZABDABC"
pattern2 = "ADA"
pattern3 = "ACA"
pattern4 = "ABDABC"
pattern5 = "DADADA"


def is_in_list(x, L):
    for i in range(len(L)-1):
        if x == L[i][0]:
            return True
    return False



def index_of(x, L):
    for i in range(len(L)):
        if x == L[i][0]:
            return L[i][1]
    return 0

#hash function
def h(s, kod):
    q = 23
    sum = 0
    j = len(s)-1
    for i in range(len(s)):
        sum += index_of(s[i], kod) * pow(4, j)
        j-=1
    return (sum % q)


def karp_rabin(T, x):
    #T - text
    #x - pattern

    kod = []

    #number of letters of the alphabet
    r = 0
    for i in range(len(T)):
        if not is_in_list(T[i], kod):
            kod.append([T[i], r])
            r += 1
    n = len(T)
    m = len(x)
    match = False
    for i in range(n-m+1):
        # K - a piece of text with the length of the pattern
        K = [None] * m
        for j in range(m):
            K[j] = T[i+j]
        if h(K, kod) == h(x, kod):
            for k in range(len(x)):
                if K[k] != x[k]:
                    match = False
                    break
                match = True
            if match:
                print("Pattern found at position "+str(i))
                return True
    print("Pattern not found")
    return False


#Tests
karp_rabin(text1, pattern1)
karp_rabin(text2, pattern2)
karp_rabin(text2, pattern3)
karp_rabin(text2, pattern4)
karp_rabin(text2, pattern5)
karp_rabin(text3, pattern4)