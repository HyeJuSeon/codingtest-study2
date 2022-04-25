import sys
input = sys.stdin.readline
N = int(input())
d = []

for i in range(N) :
    tmp = list(map(int, input().split()))
    if i == 0 :
        d.append(tmp[0])
    d.append(tmp[1])

def solution(d) :
    length = len(d) - 1 #d에서 0일때 하나 더 넣었으므로 행렬 개수는 d-1
    M = [[-1] * (length+1) for _ in range(length+1)] # 메모이제이션 실행할 배열, 0이 있으므로 안전상
    for i in range(1, length + 1) :
        M[i][i] = 0
    for i in range(1, length) :
        for j in range(1, length - i + 1) : # 5, 4, 3, 2, 1이렇게 줄어든다.
            k = i + j # 마찬가지로 length까지 늘어남 왜? 최대 j = length - i, j k쌍은 1,2, 2,3 ,3,4...처럼 대각선 방향으로 증가한다.
            M[j][k] = minimun(M,d,j,k)
    return M
def minimun(M,d,j,k) :
    minval = 2**31 - 1
    for z in range(j, k) :
        value = M[j][z] + M[z+1][k]
        value += d[j-1] * d[z] * d[k]
        if minval > value :
            minval = value
    return minval

result = solution(d)
print(result[1][-1])
