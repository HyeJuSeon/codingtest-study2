## 백준 5430 AC

### 알고리즘

```txt
 ✅ 구현
 ✅ 큐 자료구조 사용
```

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque
import sys

TC=int(input())
read=sys.stdin.readline

for _ in range(TC):
    func=read()
    n=int(read())
    # 문자열로 들어온 배열 형태를 양 끝의 꺽쇠 삭제 후 배열->큐로 만들어서 q에 저장
    # []삭제 후 빈 문자열은 배열 형태로 전환되지 않아 직접 []로 만들어줌
    arr_str=read().lstrip('[').rstrip(']')
    q=deque(arr_str.split(',')) if arr_str!='' else deque([])

    # 뒤집기 횟수를 저장할 rev_cnt
    # R을 만날 때마다 reverse함수 적용 -> 시간 초과
    # 뒤집기 횟수 저장 후 마지막에 한번에 처리하기 위함
    rev_cnt=0
    # 오류 발생 여부를 체크할 make_error
    make_error=False

    for i in func:
        if i=='R': rev_cnt+=1
        elif i=='D':
            if q:
                # 뒤집기 발생 횟수에 따라 버리기하는 부분이 달라짐
                if rev_cnt%2==0:
                    q.popleft()
                else:
                    q.pop()
            # 큐가 비어있을 경우에 원소를 빼려고 하면 오류 발생
            else:
                make_error=True
                break

    if make_error:
        print("error")
    else:
        if rev_cnt%2==0:
            print("["+",".join(q)+"]")
        else:
            # 뒤집기 횟수가 홀수인 경우 뒤집어줘야 함
            q.reverse()
            print("["+",".join(q)+"]")
```
