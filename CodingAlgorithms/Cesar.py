
def cesar(text, p):
    s = ""
    for c in text:
        if (ord(c) > 90 - p and ord(c) < 97) or ord(c) > 122 - p:
            s += chr(ord(c) + p - 26)
        else:
            s += chr(ord(c) + p)
    return s


print(cesar("abc", 1))
print(cesar("ABCD", 2))
print(cesar("XYZ", 3))
print(cesar("xyz", 2))
print(cesar("ABYZ", 8))