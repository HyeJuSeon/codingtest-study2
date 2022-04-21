import sys
input = sys.stdin.readline
MAX = sys.maxsize
N = int(input())
def solution(data, size) :
    M = [[0] * (size+1) for _ in range (size+1)]
    Sum = [0]
    for d in data :
        Sum.append(Sum[-1] + d)
    for i in range(1, size+1) :
        M[i][i] = data[i-1]
    for diag in range(1, size+1) :
        for j in range(1, size - diag + 1) : #54321순으로 줄어든다
            i = diag + j # i는 최대 size까지 늘어나야 한다. 이 방법이 바텀업 대각선 배열 표준. 기억하자.
            M[j][i] = solve(M, j, i, Sum)
    return M
def solve(M, j, i, Sum) :
    Min = MAX
    for z in range(j, i) :
        print(i+1)
        value = M[j][z] + M[z+1][i] + Sum[i] - Sum[j]
        if Min > value :
            Min = value
    return Min

for i in range(N) :
    size = int(input())
    data = list(map(int, input().split()))
    result = solution(data, size)
    print(result[1][-1])

