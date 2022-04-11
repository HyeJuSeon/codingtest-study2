## 풀이

## 코드

```import heapq
import math

def solution(jobs):
    jobs = sorted(jobs, key= lambda x : x[0])
    heap = []
    start = -1
    end = 0
    temp = 0
    answer = 0

    #작업 시작 시점부터 종료 시점 사이 작업만 힙에 넣고 최소힙을 찾아나가는 과정을 반복한다

    while len(jobs) > temp:
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(heap, (job[1],job))
                # print(heap) => [(0,[0,3]),(1,[1,9]),... ] 

        if len(heap) != 0:
            min_heap = heapq.heappop(heap)[1]
            #print(min_heap) => [0,3]

            temp+=1
            start = end
            end += min_heap[1]
            answer += end - min_heap[0]
        else:
            end+=1

    return math.floor(answer / len(jobs))
    
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

        

#요청부터 종료까지 걸리는 시간의 합의 평균이 작은 방법을 찾아야한다.
#무지성 완전탐색
#앞 작업이 끝나는 시점에 요청시간이 포함되는 경우 중 최소값을 찾는다
#위와 같은 경우가 없으면 가장 요청시간이 이른 경우를 선택
#위 값이 음수인 케이스만 제외하고 완전탐색
from itertools import permutations

'''
def solution(jobs):
    heap = []
    answer = 0
    for case in permutations(jobs):
        tar_time = 0
        front_fin_time = 0
        temp = True
        for job in case:
            req_fin_time = job[0] - front_fin_time + job[1]
            if req_fin_time < 0:
                temp = False
                break
            else:
                tar_time += req_fin_time
                front_fin_time += job[1]
            
        if temp:
            heapq.heappush(heap,tar_time)
        
    print(heapq.heappop(heap))
        
    return answer
solution([[0, 3], [1, 9], [2, 6]])
'''
```





