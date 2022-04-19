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


def boyer_moore(T, x):
    last = []
    k = len(x)-1
    for i in range(len(x)):
        if not is_in_list(x[k], last):
            last.append([x[k], k])
        k -= 1
    #Text length
    n = len(T)
    #Pattern length
    m = len(x)
    i = m - 1
    while(i < n):
        j = m-1
        while(j >= 0):
            if(x[j]==T[i]):
                if(j==0):
                    print("Pattern found at position "+str(i))
                    return True
                else:
                    i -= 1
                    j -= 1
            else:
                i += m - min(j, index_of(T[i], last))
                j = m-1
                break
    print("Pattern not found")


#Tests
boyer_moore(text1, pattern1)
boyer_moore(text2, pattern2)
boyer_moore(text2, pattern3)
boyer_moore(text2, pattern4)
boyer_moore(text2, pattern5)
boyer_moore(text3, pattern4)

