def solution(n):
    # 대각선 아래 방향, 가로 방향, 대각선 위 방향
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    numbers = n*(n+1) // 2 # 채워야할 총 숫자 개수
    layer = [[0]*i for i in range(1, n+1)] # 피라미드 형태로 뼈대 만들기
    x, y, d, num = 0, 0, 0, 1

    while num <= numbers: # 수의 범위 1 ~ 총 숫자 개수
        layer[x][y] = num
        num += 1

        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and layer[nx][ny] == 0: # 범위 안에 있으면서 방문하지 않았다면
            x = nx
            y = ny
        else:
            d = (d+1) % 3 # 조건에 막힐때마다 d+1을 통해 방향 전환
            x += dx[d]
            y += dy[d]
    
    return sum(layer, [])