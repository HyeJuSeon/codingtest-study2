## 풀이
차량별 주차장 이용 시간을 {차량번호:시간}의 딕셔너리로 정리하고 조건에 맞게 요금을 계산하는 
## 코드

```from collections import defaultdict
import math

#math.ceil => 올림
#math.floor => 버림
def solution(fees, records):
    answer = []
    car_time_dict = defaultdict(int)
    idx_list = [] #이미 계산한 차량 체크
    for i in range(len(records)-1):
        for j in range(i+1,len(records)):
            if i not in idx_list and j not in idx_list:
                in_time, in_car, _ = records[i].split()
                out_time, out_car, _ = records[j].split()
                in_hour, in_minute = map(int,in_time.split(":"))
                out_hour, out_minute = map(int,out_time.split(":"))
                if in_car == out_car:
                    passed_time = ((out_hour-in_hour)*60 + out_minute-in_minute) if out_minute >= in_minute else ((out_hour-1-in_hour)*60 + 60-(in_minute-out_minute))
                    car_time_dict[in_car] += passed_time
                    idx_list.append(i)
                    idx_list.append(j)
                    break
                else:
                    continue
            else:
                continue
                
    for i in range(len(records)):
        if i not in idx_list:
            time, car, _ = records[i].split()
            hour,minute = map(int,time.split(':'))
            car_time_dict[car] += (23-hour)*60 + 59-minute

    for car, time in sorted(car_time_dict.items(), key = lambda x : x[0]):
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+(math.ceil((time-fees[0])/fees[2])*fees[3]))
    
    return answer
```





