




row = int(input())
col = int(input())
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def solution(rows, columns, queries):
    answer = []
    field = [[0 for i in range(rows)] for j in range(columns)]
    count = 1
    for i in range(columns) :
        for j in range(rows) :
            field[i][j] = count
            count +=1

    for i in range(len(queries)) :
        tmp_result = 1000000000
        xf = queries[i][0]
        xt = queries[i][1]
        yf = queries[i][2]
        yt = queries[i][3]
        flag = 0
        for j in range(xf + 1, xt+ 1) :
            tmp = field[yf][j - 1]
            field[yf][j] = tmp
            




    return answer

solution(row, col, queries)

