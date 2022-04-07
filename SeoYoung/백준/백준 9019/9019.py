# pypy3으로 해결
from collections import deque
import sys
input = sys.stdin.readline

def bfs(A,B):
    visited=[0]*10000
    q=deque()
    q.append((A,""))
    visited[A]=1

    while q:
        node,oper=q.popleft()
        
        if node==B:
            print(oper)
            return

        num=node*2 if node*2<10000 else node*2%10000
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'D'))
            
        num=node-1 if node!=0 else 9999
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'S'))
                
        num=10*(node%1000)+node//1000
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'L'))
                
        num=1000*(node%10)+node//10
        if visited[num]==0:
            visited[num]=1
            q.append((num,oper+'R'))
            
TC=int(input())

for _ in range(TC):
    A,B=map(int, input().split())
    bfs(A,B)