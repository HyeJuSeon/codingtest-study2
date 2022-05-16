h,w,x,y = map(int, input().split())

b = [list(map(int,input().split())) for i in range(h+x)]
a = b

for i in range(h):
    for j in range(w):
        a[i+x][j+y] -= b[i][j]

for i in range(h):
    for j in range(w):
        print(a[i][j])


