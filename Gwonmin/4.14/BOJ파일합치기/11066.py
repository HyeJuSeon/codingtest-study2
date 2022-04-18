#순서대로 합치면서 간다.
#합쳐진 값이 다음에 나오는 값보다 작으면 먼저 합친다.

T = int(input())

for _ in range(T):
    k = int(input())
    dp = [[0]*(k+1) for _ in range(k+1)]
    print(dp)
    pages = list(map(int,input().split()))
    print(pages)


