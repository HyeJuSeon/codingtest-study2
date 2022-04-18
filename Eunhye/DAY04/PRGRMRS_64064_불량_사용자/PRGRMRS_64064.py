from itertools import permutations 

def check(p ,banned_id):
    for i in range(len(banned_id)):
        # 길이가 같지 않다면 다른 id
        if len(p[i]) != len(banned_id[i]):
            return False

        for j in range(len(p[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != p[i][j]:
                return False
    
    return True

def solution(user_id, banned_id):
    permu = list(permutations(user_id,len(banned_id)))
    banned = []

    for p in permu:
        if not check(p, banned_id):
            continue 
        else:
            # 중복 제거
            p = set(p)
            if p not in banned:
                banned.append(p)

    return len(banned)