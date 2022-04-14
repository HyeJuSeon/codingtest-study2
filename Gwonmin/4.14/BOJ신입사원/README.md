## 풀이

## 코드

```
#서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
#신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    result = 0
    total_lst = []
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        total_lst.append(list(map(int,sys.stdin.readline().strip().split())))
    
    total_lst.sort()
    count = 1
    paper_top = total_lst[0]

    for i in total_lst:
        if i[1] < paper_top[1]:
            paper_top = i
            count += 1
        
    print(count)
```
