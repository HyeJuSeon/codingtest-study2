from itertools import permutations

def mapping(user, ban):
    if len(user) != len(ban):
        return False
    for i in range(len(user)):
        if ban[i] != '*' and user[i] != ban[i]:
            return False
    return True

def solution(user_id, banned_id):
    ans = []
    cases = permutations(user_id, len(banned_id))
    for case in cases:
        cnt = 0
        for c, b in zip(case, banned_id):
            if mapping(c, b):
                cnt += 1
        if cnt == len(banned_id):
            case = set(case)
            if case not in ans:
                ans.append(case)
    return len(ans)

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))