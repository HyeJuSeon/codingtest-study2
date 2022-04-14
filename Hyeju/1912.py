import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = a
for i in range(1, n):
    if (d[i] < d[i - 1] + a[i]):
        d[i] = d[i - 1] + a[i]
print(max(d))