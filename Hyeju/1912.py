import sys

n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    if (d[i] < d[i - 1] + d[i]):
        d[i] = d[i - 1] + d[i]
print(max(d))