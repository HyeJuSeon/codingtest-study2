import sys


def floyd(arr, n) :
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])
def solution(n, s, a, b, fares) :
        s = s-1
        a = a-1
        b = b-1
        arr = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for i in range(n) :
            arr[i][i] = 0
        for start, end, fee in fares :
            arr[start-1][end-1] = fee
            arr[end-1][start-1] = fee
        floyd(arr, n)
        result = sys.maxsize
        for i in range(n) :
            result = min(result, arr[s][i] + arr[i][a] + arr[i][b])
        return result