def is_in_list(x, list):
    for i in list:
        if x == i:
            return True
    return False


def sort(s, p):
    sorted = False
    while not sorted:
        for i in range(len(p)-1):
            if p[i+1] > p[i]:
                temp = p[i+1]
                p[i+1] = p[i]
                p[i] = temp
                temp = s[i + 1]
                s[i + 1] = s[i]
                s[i] = temp
                sorted = False
                break
            sorted = True


def split(s, p, c):
    delta = 0
    mid = -1
    for i in range(len(p)):
        fp = 0  # first part
        sp = 0  # second part
        for j in range(i):
            fp += p[j]
        for k in range(i, len(p)):
            sp += p[k]
        new_delta = abs(sp - fp)
        if new_delta > delta and i != 0:
            break
        delta = round(new_delta, 2)
        mid += 1
    FPS = list()
    FPP = list()
    SPS = list()
    SPP = list()
    for i in range(mid):
        FPS.append(s[i])
        FPP.append(p[i])
    for j in range(mid, len(p)):
        SPS.append(s[j])
        SPP.append(p[j])

    for el in FPS:
        c[el] += '0'
    for el in SPS:
        c[el] += '1'

    if len(FPS) > 1:
        split(FPS, FPP, c)
    if len(SPS) > 1:
        split(SPS, SPP, c)


def shanon_fano(slowo):
    S = list() #Characters
    P = list() #The probabilities of the occurrence of a given character
    C = dict() #Characters codes
    for i in range(len(slowo)):
        if is_in_list(slowo[i], S):
            P[S.index(slowo[i])] += 1
        else:
            S.append(slowo[i])
            P.append(1)
    for i in range(len(P)):
        P[i] /= len(slowo)
    sort(S, P)
    for el in S:
        C[el]=""
    split(S, P, C)
    print(C)


shanon_fano("ABCDBBDDAD")
shanon_fano("AABACEDDEE")
shanon_fano("ABCD")