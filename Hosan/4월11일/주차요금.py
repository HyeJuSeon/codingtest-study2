from datetime import datetime
import math
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
times = {}
money = {}
answer = []
car_nums = set([])
for i in range(len(records)) :
    target = records[i].split()
    car_num = int(target[1])
    car_nums.add(car_num)
    hour = int(target[0][:2])
    minute = int(target[0][3:])
    if target[2] == "IN" :
        times[car_num] = [hour, minute]
    if target[2] =="OUT" :
        from_hour = times[car_num][0]
        from_min = times[car_num][1]
        to_hour = hour
        to_min = minute
        if to_min - from_min < 0 :
            to_hour -= 1
            to_min += 60
        result = ((to_hour - from_hour) * 60) + (to_min - from_min)
        if car_num in money.keys() :
            money[car_num] += result
        else :
            money[car_num] = result
        times.pop(car_num)
if times != {} :
    for i in times.keys() :
        hour = times[i][0]
        minute = times[i][1]
        result = ((23 - hour) * 60) + (59 - minute)
        if i in money.keys():
            money[i] += result
        else:
            money[i] = result
for car in money.keys() :
    time_length = money[car]
    if time_length <= fees[0] :
        money[car] = fees[1]
    else :
        result = fees[1]
        time_length -= fees[0]
        result += math.ceil(time_length/fees[2]) * fees[3]
        money[car] = result
List = list(car_nums)

for car in List :
    answer.append(money[car])
print(money)
print(answer)

