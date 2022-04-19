def is_in_list(x, list):
    for i in list:
        if x == i:
            return True
    return False

def sort(s, p):
    sorted = False
    while not sorted:
        for i in range(len(p)-1):
            if p[i] > p[i+1]:
                temp = p[i+1]
                p[i+1] = p[i]
                p[i] = temp
                temp = s[i + 1]
                s[i + 1] = s[i]
                s[i] = temp
                sorted = False
                break
            sorted = True

def find(T, x):
    match = False
    for i in range(len(T) - len(x)+1):
        if T[i] == x[0]:
            for j in range(len(x)):
                if T[i+j] != x[j]:
                    match = False
                    break
                match = True
        if match:
            break
    if match:
        return True
    else:
        return False

def huffman(slowo):
    S = list() #Characters
    P = list() #The probabilities of the occurrence of a given character
    TS = list() #Characters tree
    TP = list() #Probabilities tree
    C = dict() #Characters codes

    #Building a character tree for Huffman code
    for i in range(len(slowo)):
        if is_in_list(slowo [i], S):
            P[S.index(slowo[i])] += 1
        else:
            S.append(slowo[i])
            P.append(1)
    for i in range(len(P)):
        P[i] /= len(slowo)
    sort(S, P)
    TS.append(S.copy())
    TP.append(P.copy())
    while(len(S) > 2):
        s = S.pop(0)+S.pop(0)
        S.append(s)
        p = P.pop(0)+P.pop(0)
        P.append(round(p, 6))
        sort(S, P)
        TS.append(S.copy())
        TP.append(P.copy())

    #Creating a code for each character from a tree
    n = len(TS)-1
    for e in TS[0]:
        C[e] = ''
        for i in range(n, -1, -1):
            for j in range(len(TS[i])):
                if find(TS[i][j], e):
                    if j == 0:
                        C[e] += '0'
                    elif j == 1:
                        C[e] += '1'
                    if len(TS[i][j]) == 1:
                        break
    # Listing the tree and code
    print(TS)
    print(TP)
    print(C)
    #Converting consecutive characters of a word to their coded versions
    kod = ""
    for e in slowo:
        kod+=C[e]
    #Listing the word and its coded version
    print(slowo+" -> "+kod)

# huffman("ABCDBBDDAD")
# huffman("Zakodowany tekst")
huffman("acbbadccabcbadeabeab")
