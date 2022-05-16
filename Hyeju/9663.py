import sys

N = int(sys.stdin.readline())
col = [0 for _ in range(N)]
rd = [0 for _ in range(N * 2)]
ld = [0 for _ in range(N * 2)]
ans = 0

def backtracking(c):
    global ans
    if c == N:
        ans += 1
        return
    for i in range(N):
        if col[i] or rd[i + c] or ld[c - i + N - 1]:
            continue
        col[i] = rd[i + c] = ld[c - i + N - 1] = 1
        backtracking(c + 1)
        col[i] = rd[i + c] = ld[c - i + N - 1] = 0

backtracking(0)
print(ans)