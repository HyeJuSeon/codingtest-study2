## 풀이
주어진 숫자를 큐에 넣고 돌리며 0을 만날때마다 지나온 숫자들이 조건에 맞는지 확인
## 코드

```from collections import deque
import math
# 0P0처럼 소수 양쪽에 0이 있는 경우
# P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
# 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
# 예를 들어, 101은 P가 될 수 없습니다.

#큐
#정수 n의 k진수 변환
#숫자 추가 삭제 편하게 문자열로 변환
#소수 판별 함수 만들기
#0을 만나면 스택에 들어온 숫자가 문제의 조건에 맞는지 판별
#int() 함수 안에 빈 문자열이 들어가면 오류남 ex) ""

def solution(n, k):
    answer = 0

    dq = deque()
    while n >= k:
        dq.appendleft(str(n%k))
        n = n // k
        if n < k:
            dq.appendleft(str(n))

    #변환된 수    
    num_str = ""
    while len(dq) != 0:
        if dq[0] != "0":
            num_str += dq.popleft()
        else:
            dq.popleft()
            if num_str == "":
                continue
            
            num = int(num_str)
            if check_prime(num):
                answer += 1
            num_str = ""

    if num_str != "" and check_prime(int(num_str)):
        answer += 1

    
    return answer

def check_prime(num):
    if num == 1:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True
```





