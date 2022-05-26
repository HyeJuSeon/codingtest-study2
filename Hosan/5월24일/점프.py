import sys
input = sys.stdin.readline

def solution(field, i, j) :
    if i == 1 and j == 1 :
        return 1
    tmp_i = i - 1
    tmp_j = j - 1
    result = 0
    while tmp_i > 0 :
        if field[tmp_i][j] + tmp_i == i :
            result += solution(field, tmp_i, j)
        tmp_i -= 1
    while tmp_j > 0 :
        if field[i][tmp_j] + tmp_j == j :
            result += solution(field, i, tmp_j)
        tmp_j -= 1
    return result

N = int(input())
field = [[0 for _ in range(N+1)]for _ in range(N+1)]
count = [[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(1, N+1) :
    tmp = list(map(int, input().split()))
    for j in range(1, N+1) :
        field[i][j] = tmp[j-1]
count[1][1] = 1 #기저조건
for i in range(1, N+1) :
    for j in range(1, N+1) :
        tmp = field[i][j]
        if i + tmp < N + 1 and tmp > 0:
            count[i+tmp][j] += count[i][j]
        if j + tmp < N + 1 and tmp > 0:
            count[i][j+tmp] += count[i][j]
print(count[N][N])
