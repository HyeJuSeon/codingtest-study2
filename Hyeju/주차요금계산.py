import math
from collections import defaultdict
def solution(fees, records):
    dt, df, ut, uf = fees
    in_car = {}
    dic = defaultdict(int)
    for record in records:
        time, car, inout = record.split(' ')
        if inout == 'IN':
            in_car[car] = time
        else:
            h1, m1 = map(int, in_car.pop(car).split(':'))
            h2, m2 = map(int, time.split(':'))
            t = (h2 - h1) * 60 + m2 - m1
            dic[car] += t
    for c in in_car:
        h, m = map(int, in_car[c].split(':'))
        t = (23 - h) * 60 + 59 - m
        dic[c] += t
    dic = sorted(dic.items())
    ans = []
    for d in dic:
        t = int(d[1])
        f = df
        if t > dt:
            f += math.ceil((t - dt) / ut) * uf
        ans.append(f)
    return ans

# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))