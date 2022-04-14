from collections import defaultdict

def convert(s):
    hr, mn = s.split(":")
    return int(hr)*60+int(mn)

def calc_fee(fees, t):
    if t <= fees[0]:
        return fees[1]
    fee = fees[1] +((t-fees[0])//fees[2]) * fees[3]
    return fee + fees[3] if (t-fees[0])%fees[2] else fee

def solution(fees, records):
    cumul_time = defaultdict(list)
    status_dict = dict()
    result = []
    for rcd in records:
        time, car_num, status = rcd.split()
        if status == "IN":
            cumul_time[car_num].append(convert(time))
            status_dict[car_num] = 1
        else:
            cumul_time[car_num].append(convert(time)-cumul_time[car_num].pop())
            status_dict[car_num] = 0

    for car in cumul_time.keys():
        if status_dict[car]:
            cumul_time[car].append(convert("23:59")-cumul_time[car].pop())
            status_dict[car] = 0
        result.append((car, calc_fee(fees, sum(cumul_time[car]))))

    result.sort()
    return [res[1] for res in result]