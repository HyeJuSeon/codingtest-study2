import sys
from collections import deque

MOD = 10000
T = int(sys.stdin.readline())

def Visit(i, op):
    if not visit[i]:
        visit[i] = True
        q.append((i, ans + op))

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    q = deque()
    q.append((A, ''))
    visit = [False] * 10000

    while q:
        curr, ans = q.popleft()
        visit[curr] = True
        if curr == B:
            print(ans)
            break

        num = (2 * curr) % MOD
        Visit(num, 'D')
        num = (curr - 1) % MOD
        Visit(num, 'S')
        num = (curr * 10 + curr // 1000) % MOD
        Visit(num, 'L')
        num = (curr // 10 + (curr % 10) * 1000) % MOD
        Visit(num, 'R')
