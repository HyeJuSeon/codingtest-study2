'''프로그래머스 - 주차 요금 계산 '''

from collections import defaultdict
import math

# 총 주차 시간(분)을 구하는 함수
def cal_time(in_time, out_time):
    in_time = int(in_time.split(":")[0]) * 60 + int(in_time.split(":")[1])
    out_time = int(out_time.split(":")[0]) * 60 + int(out_time.split(":")[1])
    
    return out_time - in_time

def solution(fees, records):
    base_min, base_fee, unit_min, unit_fee = fees
    record_time_dic = defaultdict(int)
    
    in_record_dic = {}
    out_record_dic = defaultdict(int) # 차량 출입 기록 딕셔너리 {"차번호": 입차(0) or 출차(1)}
    for rec in records:
        time, car_num, in_out = rec.split()
        if in_out == "IN":
            in_record_dic[car_num] = time
            out_record_dic[car_num] = 0 # 입차 처리
        elif in_out == "OUT":
            in_time = in_record_dic[car_num]
            rec_time = cal_time(in_time, time)
            record_time_dic[car_num] += rec_time # 차 번호별 주차시간 저장
            out_record_dic[car_num] = 1 # 출차 처리
            
    # for문 다 돌았는데 기록이 남아있으면 23:59에 출차한 것으로 처리
    for car_num, out_rec in out_record_dic.items():
        if out_rec == 0: # 입차가 기록된 차가 있는 경우
            out_time = "23:59"
            in_time = in_record_dic[car_num]
            rec_time = cal_time(in_time, out_time)
            record_time_dic[car_num] += rec_time
    
    result = []
    for car_num, rec_time in record_time_dic.items():
        if rec_time < base_min: # 기본 시간의 범위에 해당하는 경우 => 기본 요금
            fee = base_fee
        else: # 기본 시간을 넘어가는 경우 => 기본요금 + 추가한 시간에 대한 요금
            fee = base_fee + math.ceil((rec_time - base_min) / unit_min) * unit_fee
        result.append((int(car_num), fee))
    
    result.sort(key=lambda x: (x[0])) # 차 번호가 작은 숫자순으로 요금 정렬
    return [i[1] for i in result]