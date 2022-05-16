def solution(n):
    map = [[0 for _ in range(i + 1)] for i in range(n)]
    x, y, num = -1, 0, 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            map[x][y] = num
            num += 1
    ans = sum(map, [])
    return ans

# print(solution(4))
# print(solution(5))
# print(solution(6))