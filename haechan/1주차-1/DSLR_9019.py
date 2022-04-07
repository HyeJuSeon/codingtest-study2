'''백준 9019 - DSLR'''

from collections import deque
import sys

def get_command_bfs(a, b, memory):
    dq = deque([("", a)])
    memory[a] = True

    while dq: # D -> S -> L -> R 반복 진행
        command, now_a = dq.popleft()
        if now_a == b:
            return command

        next_a = (now_a * 2) % 10000
        if not memory[next_a]:
            memory[next_a] = True
            dq.append((command + "D", next_a))

        next_a = (now_a - 1) % 10000 # -1 % 10000 = 9999
        if not memory[next_a]:
            memory[next_a] = True
            dq.append((command + "S", next_a))

        next_a = (now_a % 1000) * 10 + now_a // 1000 # 1234 % 1000 -> 234 * 10 -> 2340 + 1234 // 1000 -> 2341
        if not memory[next_a]:
            memory[next_a] = True
            dq.append((command + "L", next_a))

        next_a = (now_a % 10) * 1000 + now_a // 10 # 1234 -> 4000 + 123
        if not memory[next_a]:
            memory[next_a] = True
            dq.append((command + "R", next_a))

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    memory = [False] * 10000
    print(get_command_bfs(a, b, memory))
