# 새로운 언어 AC - 정수 배열에 연산을 하기 위해 만든 언어(뒤집기, 버리기 가능)
# R은 배열의 순서를 뒤집는 함수, D는 첫번쨰 수 버리는 함수(비어있는데 버리면 에러 발생)
# 함수는 조합해서 사용 가능
from collections import deque
import sys

TC=int(input())
read=sys.stdin.readline

for _ in range(TC):
    func=read()
    n=int(read())
    arr_str=read().lstrip('[').rstrip(']')
    rev_cnt=0
    
    q=deque(arr_str.split(',')) if arr_str!='' else deque([])
    make_error=False
    
    for i in func:
        if i=='R': rev_cnt+=1
        elif i=='D':
            if q:
                if rev_cnt%2==0:
                    q.popleft()
                else:
                    q.pop()
            else: 
                make_error=True
                break
    
    if make_error:
        print("error")
    else:
        if rev_cnt%2==0:
            print("["+",".join(q)+"]")
        else:
            q.reverse()
            print("["+",".join(q)+"]")