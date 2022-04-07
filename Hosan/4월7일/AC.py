import sys
input = sys.stdin.readline

N = int(input())

for i in range(N) :
    order = input()
    length = int(input())
    if length == 0 :
        contents = []
        trash = input()
    else :
        contents = input().rstrip()[1:-1].split(",")
    flag = 0
    rev = 2
    for j in range(len(order)) :
        if order[j] == 'R' :
            rev += 1
        elif order[j] == 'D' :
            if len(contents) < 1:
                print("error")
                flag = 1
                break
            if rev % 2 == 0:
                contents.pop(0)
            else:
                contents.pop(-1)
    if rev % 2 != 0 :
        contents.reverse()
    if flag == 0:
            print("[" + ",".join(contents) + "]")