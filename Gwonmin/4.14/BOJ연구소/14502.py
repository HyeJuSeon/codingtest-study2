#2차원 배열 디버깅 방법
# print(*M, sep="\n")

#벽을 세운다
#바이러스를 퍼트린다
#안전 영역의 크기를 계산한다
n,m = map(int,input().split())

M = []
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤 사용할 리스트

for _ in range(n):
    M.append(list(map(int,input().split())))

#바이러스를 퍼트리기 위한 방향벡터
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0
test = M

def virus(x,y):
    #사방으로 퍼지게 하기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #상하좌우 경계를 넘어가지 않는 경우
        if nx >= 0 and nx < n and ny >=0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny) #재귀적으로 퍼트리기

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    #벽 3개 만든 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = M[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
    
        result = max(get_score(),result)
        return

    for i in range(n):
        for j in range(m):
            if M[i][j] == 0:
                M[i][j] = 1
                count += 1
                dfs(count)
                M[i][j] = 0
                count -= 1
    
dfs(0)
print(result)