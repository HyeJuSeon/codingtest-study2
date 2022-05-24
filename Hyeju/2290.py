import sys

s, n = map(str, sys.stdin.readline().split())
s = int(s)
l = len(n)
ans = [[' ' for _ in range((s + 3) * l)] for _ in range(2 * s + 3)]

def vertical(top, bottom, second):
    global s, c
    if top:
        for i in range(1, s + 1):
            ans[i][c] = '|'
    if bottom:
        for i in range(s + 2, 2 * s + 2):
            ans[i][c] = '|'
    if second:
        c += s + 1
        t, b = second
        vertical(t, b, 0)
        c -= s + 1

def horizontal(top, mid, bottom):
    global s, c
    c += 1
    for i in range(c, c + s):
        if top:
            ans[0][i] = '-'
        if mid:
            ans[s + 1][i] = '-'
        if bottom:
            ans[-1][i] = '-'
    c += s

func = [vertical, horizontal]
params = { '2': [(0, 1, (1, 0)), (1, 1, 1)], '3': [(1, 1, 0), (1, 1, 1)], '4': [(1, 0, (1, 1)), (0, 1, 0)],
           '5': [(1, 0, (0, 1)), (1, 1, 1)], '6': [(1, 1, (0, 1)), (1, 1, 1)], '7': [(1, 1, 0), (1, 0, 0)],
           '8': [(1, 1, (1, 1)), (1, 1, 1)], '9': [(1, 0, (1, 1)), (1, 1, 1)], '0': [(1, 1, (1, 1)), (1, 0, 1)] }
c = 0
for i in str(n):
    if i == '1':
        c += s + 1
        vertical(1, 1, 0)
    elif i == '3' or i == '7':
        for f, p in zip(func[::-1], params[i][::-1]):
            x, y, z = p
            f(x, y, z)
    else:
        for f, p in zip(func, params[i]):
            x, y, z = p
            f(x, y, z)
    c += 2

for i in range(2 * s + 3):
    for j in range((s + 3) * l):
        print(ans[i][j], end='')
    print()
