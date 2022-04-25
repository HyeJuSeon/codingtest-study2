from collections import Counter
def solution(str1, str2):
    answer = 0
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i:i+2].upper())
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            s2.append(str2[j:j+2].upper())       
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    intersection = len(list((cnt1 & cnt2).elements()))
    union = len(list((cnt1 | cnt2).elements()))

    return 65536*intersection // union if union else 65536