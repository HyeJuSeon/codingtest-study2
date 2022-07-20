## 풀이

permutations 모듈을 사용하여 구현해주었습니다.

check 함수를 만들어 해당 아이디가 불량사용자 아이디인지 체크해주었습니다.

불량사용자 아이디가 아니라면 continue로 넘겨주고, 불량사용자 아이디라면 중복을 제거하고 banned list에 없을 경우에만 넣어주었습니다.

마지막에는 banned의 길이를 return 해주었습니다.

## 코드

```python
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
```
