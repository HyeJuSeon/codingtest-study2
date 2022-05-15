# 크기가 h*w인 배열 a와 두 정수 x,y가 있을 때 
# (h+x)*(w+y)인 배열 b는 배열 a를 아래로 x칸, 오른쪽으로 y칸 이동시킨 배열을 겹쳐 만들 수 있다
# 배열 b의 i,j= 

H,W,X,Y=map(int, input().rstrip().split())
graph=[list(map(int,input().rstrip().split())) for _ in range(H+X)]
answer=[[0 for _ in range(W)] for _ in range(H)]
check=[[0 for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i<H and j<W: check[i][j]+=1
        # 겹치는 부분 체크
        if i+X<H and j+Y<W : check[i+X][j+Y]+=1

for i in range(H):
    for j in range(W):
        if check[i][j]==1: 
            answer[i][j]=graph[i][j]
        elif check[i][j]==2:
            answer[i][j]=graph[i][j]-answer[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(answer[i][j],end=' ')
    print()
