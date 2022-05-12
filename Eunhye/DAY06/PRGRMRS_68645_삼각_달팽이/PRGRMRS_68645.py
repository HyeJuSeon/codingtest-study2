def solution(n):
    snail = [[0 for _ in range(i)] for i in range(1,n+1)]
    total = sum(range(1,n+1))
    num, move = 1, n-1
    i, j = -2, -1
    while num <= total:
        i += 2
        j += 1
        if num == total:
            snail[i][j] = num
            break
        for _ in range(move):
            snail[i][j] = num
            num += 1
            i += 1
        for _ in range(move):
            snail[i][j] = num
            num += 1
            j += 1
        for _ in range(move):
            snail[i][j] = num
            num += 1
            i -= 1
            j -= 1
        move -= 3
    
    answer = []
    for k in range(n): answer.extend(snail[k])
    return answer