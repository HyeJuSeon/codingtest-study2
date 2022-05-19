# 다양한 크기를 가진 정사각형 모양의 하얀색, 혹은 파란색 색종이를 만들려고 함

N=int(input())
paper=[list(map(int,input().split())) for _ in range(N)]
result=[]
def isPaper(start, n):
    x, y= start
    color=paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 여러 색이 섞여 있어 색종이가 아닐 때 => 나눠줘야 함
            if color!=paper[i][j]:
                isPaper([x,y],n//2)
                isPaper([x,y+n//2],n//2)
                isPaper([x+n//2, y],n//2)
                isPaper([x+n//2,y+n//2],n//2)
                return 
    # 흰색 색종이일 때
    if color==0:
        result.append(0)
    # 파란색 색종이일 때
    else:
        result.append(1)

isPaper([0,0],N)
print(result.count(0))
print(result.count(1))
