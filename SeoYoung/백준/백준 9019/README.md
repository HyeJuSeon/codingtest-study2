## 백준 9019 DSLR

### 알고리즘

```txt
 ✅ BFS
```

### 코드 구현

사용 언어 : **파이썬**

```python
# pypy3으로 해결
from collections import deque
import sys
input = sys.stdin.readline

def bfs(A,B):
    visited=[0]*10000
    q=deque()
    # 큐에 현재 노드와 현재 노드까지 오기위한 명령어를 함께 저장함
    q.append((A,""))
    visited[A]=1

    while q:
        node,oper=q.popleft()

        # 현재 노드가 도착점이면 명령어 문자열 출력 후 함수 종료
        if node==B:
            print(oper)
            return
        # 'D'
        num=node*2 if node*2<10000 else node*2%10000
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'D'))
        # 'S'
        num=node-1 if node!=0 else 9999
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'S'))
        # 'L'
        # 처음에는 L,R 수행하기 위해 deque.rotate 사용했으나 시간초과남
        num=10*(node%1000)+node//1000
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'L'))
        # 'R'
        num=1000*(node%10)+node//10
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'R'))

TC=int(input())

for _ in range(TC):
    A,B=map(int, input().split())
    bfs(A,B)
```
