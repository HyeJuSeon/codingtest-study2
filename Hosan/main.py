import sys
sys.setrecursionlimit(10**6)

size = int(input())

field = [["x" for _ in range(size)] for _ in range(size)]

def star(size, flag, field, x, y) :
    if size == 1 :

        if flag == True :
            field[x][y] = "*"
        else :
            field[x][y] = " "
    else :
        count = 0
        for i in range(x, size + x, int(size/3)) :
            for j in range(y, size + y, int(size/3)) :
                if count == 4 :
                    star(int(size/3), False, field, i, j)
                else :
                    star(int(size/3), flag, field, i, j)
                count += 1
star(size, True, field, 0, 0)
for i in range(len(field)) :
    for j in range(len(field)) :
        print(field[i][j], end = "")
    print("")