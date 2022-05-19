def quadtree(n, y, x):
    if n == 1: 
        return [paper[y][x]]
    check = True
    for i in range(y, y+n):
        if not check:
            break
        for j in range(x, x+n):
            if paper[y][x] != paper[i][j]:
                check = False
                break
    if check:
        return [paper[y][x]]
    new_n = n // 2
    ret = quadtree(new_n, y, x) + quadtree(new_n, y, x+new_n) + quadtree(new_n, y+new_n, x) + quadtree(new_n, y+new_n, x+new_n)
    return ret

C = int(input())
paper = [ list(map(int, input().split())) for _ in range(C)]
result = quadtree(C, 0, 0)
blue = sum(result)
print(len(result)-blue)
print(blue)