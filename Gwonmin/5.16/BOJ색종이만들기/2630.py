#다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.
#n/2만큼씩 정사각형 나누기
#정사각형의 첫번재 좌표(x,y)를 반복문 돌리면서 색깔 판별
#반복문이 끝까지 돌았으면 다른 색이 없다는 것이므로 첫번째 좌표의 색깔을 꺼내 확인 후 카운트
#다른 색이 있는 경우 재귀적으로 함수를 호출해 위의 과정 반복
#분할 정복

n = int(input())
m = [list(map(int,input().split())) for i in range(n)]
white = 0
blue = 0

def solution(x, y, n):
    global white,blue
    color = m[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != m[i][j]:
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0,0,n)
print(white)
print(blue)
