import sys

N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0
def sol(r, c, n):
    global white_cnt, blue_cnt
    color = map[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if map[i][j] != color:
                sol(r, c, n // 2)
                sol(r, c + n // 2, n // 2)
                sol(r + n // 2, c, n // 2)
                sol(r + n // 2, c + n // 2, n // 2)
                return
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1

sol(0, 0, N)
print(white_cnt, blue_cnt, sep='\n')
