import math

def solution(fees, records):
    answer=[]
    # dt=기본 시간, dr=기본 요금, ut=단위 시간, ur=단위 요금
    dt, dr, ut, ur=fees
    # dic[차량번호]=누적 주차 시간 
    dic={}
    for record in records:
        # time=입차/출차 시각, number=차량 번호, check=출차여부
        time, number, check=record.split(' ')
        time = time.split(':')
        # time 문자열을 쪼개서 분 단위의 시간으로 변환 
        minutes = int(time[0])*60 + int(time[1])
        
        # 누적 주차 시간은 출차시간(분)-입차시간(분)으로 계산되어야 함
        # 입차 시 => [-minutes, False] => 입차만 하고 출차는 안되는 차를 처리하기 위해 boolean값 같이 저장
        if check=='IN':
            if number not in dic: 
                dic[number]=[-minutes,False]
            else:
                dic[number][0]-=minutes
                dic[number][1]=False
        # 출차 시
        else:
            dic[number][0]+=minutes
            dic[number][1]=True
    
    for _,value in sorted(dic.items()):
        # 입차만 되고 출차가 안된 차량이면 출차시간을 23:59로 간주 => 분으로 변환 시 1439
        if value[1]==False:
            value[0]+=1439

        totalRate=0
        # 누적 주차 시간이 기본 시간을 초과하면 초과한 시간에 대해 단위시간마다 단위요금 청구하여 계산
        if value[0]>dt:
            totalRate=dr+math.ceil((value[0]-dt)/ut)*ur
        # 아니면 기본 요금만 청구
        else:
            totalRate=dr
            
        answer.append(totalRate)        
    
    return answer