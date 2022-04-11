'''프로그래머스 - 디스크 컨트롤러

- 작업 소요시간이 짧은 것부터 먼저 수행 ==> 가장 짧은 평균 소요시간
'''

import heapq

def solution(jobs):
    length = len(jobs)
    
    result = 0
    time = 0
    jobs.sort() # 작업이 요청되는 시점이 빠른 순으로 정렬
    task_queue = []
    while len(jobs) != 0 or len(task_queue) != 0:
        while len(jobs) != 0 and jobs[0][0] <= time:
            heapq.heappush(task_queue, jobs.pop(0)[::-1]) # 작업 소요시간이 짧은 순으로 정렬되게 뒤집어 push
        
        if len(task_queue) == 0: # 힙이 비어있으면 다음 job이 요청되는 시간으로 time 할당
            time = jobs[0][0]
            continue

        spend_time, stay_time = heapq.heappop(task_queue)
        time += spend_time
        result += time - stay_time # 대기시간을 제거한 총 소요시간

    return result // length