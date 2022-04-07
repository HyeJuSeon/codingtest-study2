import sys
input = sys.stdin.readline
from collections import Counter

col, row, inv = map(int, input().split(" "))
field = []

result = 100000000
result_height = -1

def solution(field, height, inv) :
    tmp_inv = inv
    sec = 0
    for i in field :
        if i < height :
            tmp = height - i
            sec += tmp
            tmp_inv -= tmp
        elif i > height :
            tmp = i - height
            sec += tmp * 2
            tmp_inv += tmp
    if tmp_inv < 0 :
        return -1, -1
    return sec, height

for line in range(col) :
    tmp = list(map(int, input().split(" ")))
    field.extend(tmp)

counter = Counter(field)
low = min(counter.keys())
high = max(counter.keys())

for height in range(low, high + 1) :
    sec, hresult = solution(field, height, inv)
    if sec < 0 :
        continue
    elif sec < result :
        result = sec
        result_height = hresult
    elif sec == result :
        if hresult > result_height :
            result = sec
            result_height = hresult
print(result, result_height)



