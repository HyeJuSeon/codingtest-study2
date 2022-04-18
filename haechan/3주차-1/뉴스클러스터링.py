def get_alpha(string):
    tmp = []
    for i in range(0, len(string)):
        if string[i:i+2].isalpha() and " " not in string[i:i+2] and len(string[i:i+2]) == 2:
            tmp.append(string[i:i+2].upper())
    return tmp

def solution(str1, str2):
    A = get_alpha(str1)
    B = get_alpha(str2)
    string_set = set(A + B) # 중복 제거한 모든 문자열
    
    if A == [] and B == []:
        return 65536
    
    intersection = 0
    for i in string_set:
        intersection += min(A.count(i), B.count(i))
    union = len(A) + len(B) - intersection # 전체 개수 - 교집합 개수
    
    return int((intersection / union) * 65536)