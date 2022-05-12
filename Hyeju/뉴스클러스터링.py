from collections import Counter

def solution(str1, str2):
    MUL = 65536
    str1 = str1.lower()
    str2 = str2.lower()
    l1, l2 = [], []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            l1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            l2.append(str2[i:i + 2])
    c1 = Counter(l1)
    c2 = Counter(l2)
    inter = list((c1 & c2).elements())
    union = list((c1 | c2).elements())
    if not union:
        return MUL
    return int(len(inter) / len(union) * MUL)

# print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))
# print(solution('E=M*C^2', 'e=m*c^2'))