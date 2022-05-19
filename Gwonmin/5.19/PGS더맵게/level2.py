import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    # 모든 원소 힙에 삽입
    for i in scoville:
        heapq.heappush(heap, i)

    mix = 0

    while True:
        if heap[0] < K:
            if len(heap) == 1:
                answer = 0
                break
            else:
                mix = heapq.heappop(heap) + heapq.heappop(heap) * 2
                heapq.heappush(heap, mix)
                answer += 1
        else:
            break

    if answer == 0:
        return -1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))

