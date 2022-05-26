import re
def solution(s):
    ans = s.capitalize().split()[0]
    for w in re.findall(r'\s+\w+', s):
        tmp = w.strip()
        ans += w.replace(tmp, tmp.capitalize())
    return ans + s[len(ans):]

# print(solution("3people unFollowed me"))
# print(solution("for the last week"))
# print(solution("fOr The LAst week"))
# print(solution("aaaaa aaa"))