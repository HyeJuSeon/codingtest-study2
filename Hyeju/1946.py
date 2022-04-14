import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    a = []
    for _ in range(N):
        p, i = map(int, sys.stdin.readline().split())
        a.append((p, i))
    a.sort()
    ans = 1
    min = a[0][1]
    for i in range(1, N):
        if min > a[i][1]:
            min = a[i][1]
            ans += 1
    print(ans)