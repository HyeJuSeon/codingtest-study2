import heapq

def solution(scoville, k) :
    result = 0
    heapq.heapify(scoville)
    while scoville[0] < k :
        try :
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) *2)
            result += 1
        except IndexError :
            return -1
    return result 