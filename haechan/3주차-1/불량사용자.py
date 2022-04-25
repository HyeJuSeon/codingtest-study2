from itertools import permutations

# 해당 case의 user_id가 banned_id에 해당하는지 여부 확인
def checked_id(case, banned_id):
    flag = True
    for i in range(len(case)):
        if len(case[i]) == len(banned_id[i]):
            for s1, s2 in zip(case[i], banned_id[i]):
                if s1 != s2 and s2 != "*":
                    flag = False
        else:
            flag = False
    
    return flag
    
def solution(user_id, banned_id):
    cases = permutations(user_id, len(banned_id)) # 전체 경우의 수
    
    case_set = []
    for case in cases:
        # 고유한 값인지 판단하기 위해 set() 사용
        # [(1, 2, 3), (3, 2, 1)] => [{1, 2, 3}, {1, 2, 3}]
        if checked_id(case, banned_id) and set(case) not in case_set:
            case_set.append(set(case))
            
    return len(case_set)