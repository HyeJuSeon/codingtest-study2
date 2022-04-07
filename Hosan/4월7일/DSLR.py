import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    visited = [0] * 10000
    deq = deque()
    deq.append([a, ""])
    visited.append(a)
    while deq :
        cur, bef = deq.popleft()
        if cur == b :
            print(bef)
            break
        else :
            tmp_d = (2*cur)%10000
            tmp_s = cur-1 if cur!=0 else 9999
            tmp_l = 10*(cur%1000) + cur//1000
            tmp_r = R_num = 1000*(cur%10) + cur//10
            if visited[tmp_d] == 0 :
                deq.append([tmp_d, bef + "D"])
                visited[tmp_d] = 1
            if visited[tmp_s] == 0 :
                deq.append([tmp_s, bef + "S"])
                visited[tmp_s] = 1
            if visited[tmp_l] == 0 :
                deq.append([tmp_l, bef + "L"])
                visited[tmp_l] = 1
            if visited[tmp_r] == 0 :
                deq.append([tmp_r, bef + "R"])
                visited.append(tmp_r)
                visited[tmp_r] = 1