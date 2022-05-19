import sys

H, W, X, Y = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(H + X)]

for i in range(X, H):
    for j in range(Y, W):
        B[i][j] -= B[i - X][j - Y]

for i in range(H):
    print(' '.join(map(str, B[i][:W])))