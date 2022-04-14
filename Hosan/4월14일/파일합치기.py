import sys
input = sys.stdin.readline
import math

N = int(input())

def solution(data, size) :
    M = [[-1] * (size+1) for _ in range (size+1)]
    for i in range(1, size+1) :
        M[i][i] = data[i-1]
    for diag in range(1, size+1) :
        for j in range(1, size - diag + 1) : #54321순으로 줄어든다
            i = diag + j # i는 최대 size까지 늘어나야 한다. 이 방법이 바텀업 대각선 배열 표준. 기억하자.
            M[j][i] = solve(data, M, j, i)
    return M

def solve(data, M, j, i) :
    Min = 2000000000
    for z in range(j, i) :
        value = M[j][z] + M[z+1][i]
        if Min > value:
            Min = value
    return Min

for i in range(N) :
    size = int(input())
    data = list(map(int, input().split()))
    result = solution(data, size)
    print(result)
    print(result[1][-1] + sum(data))