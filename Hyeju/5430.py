import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().strip()[1:-1].split(','))
    if n == 0:
        arr = deque()

    r_cnt = 0 # reverse 메소드 -> 시간 초과 때문에 r_cnt 변수 선언
    err = False
    for i in p:
        if i == 'R':
            r_cnt += 1
        elif i == 'D':
            if arr:
                if r_cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                err = True
                break
    if r_cnt % 2 == 1:
        arr.reverse()
    if not err:
        print(f'[{",".join(arr)}]')
