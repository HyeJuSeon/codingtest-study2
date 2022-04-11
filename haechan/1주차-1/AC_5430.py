'''백준 5430 - AC'''

from collections import deque
import ast

# RDRDRDRD... 계속 번갈아 나오는 경우 계속 reverse해야하므로 시간초과 => 직접 바꾸는 건 반환할 때
def result_func(p, arr):
    reverse = 1 # 정방향
    dq = deque(arr)
    for function in p:
        if function == "R":
            reverse *= -1 # 역방향
        elif function == "D":
            if not dq:
                return "error"
            if reverse == 1: # True
                dq.popleft()
            elif reverse == -1: # False
                dq.pop()
    
    # 반환할 떄 배열 순서를 맞춰줘야돼.. !
    if reverse == -1:
        dq.reverse()
    arr_str = str(list(dq))[1:-1].replace(" ", "").split(",")
    result = "[" + ",".join(arr_str) + "]"
    return result

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = ast.literal_eval(input()) # 문자열 형태의 리스트를 리스트 타입으로 변경

    print(result_func(p, arr))