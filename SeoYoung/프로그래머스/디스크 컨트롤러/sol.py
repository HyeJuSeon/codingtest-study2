import heapq
def solution(jobs):
    n=len(jobs)
    answer,curTime,i = 0,0,0
    start=-1
    # jobs를 요청 시간 순으로 처리
    jobs=sorted(jobs,key=lambda x:x[0])
    pq=[]
    
    heapq.heapify(pq)
    
    while i<len(jobs):
        # 현재 시점에서 가능한 작업들 큐에 넣어주기
        for j in jobs[i:]:
            # 이전 작업 종료 시간< 작업 시작시간<=현재시간이면 힙에 [작업시간, 시작시간] 넣어줌 
            # (최소 작업시간이 pq[0]이어야 함)
            if start<j[0]<=curTime: 
                heapq.heappush(pq,[j[1],j[0]])
        # 큐가 비어 있지 않으면(현재 할 수 있는 작업들이 있는 것)
        # 작업하고 start, curTime, answer, i 업데이트
        if len(pq)>0:
            curTask=heapq.heappop(pq)
            start=curTime
            curTime+=curTask[0]
            answer+=(curTime-curTask[1])
            i+=1
        # 할 수 있는 작업이 없으면 현재 시간 + 1
        else:
            curTime+=1
    
    return answer//n