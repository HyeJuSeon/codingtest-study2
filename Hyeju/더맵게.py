import heapq

def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        ans += 1
    if scoville[0] < K:
        return -1
    return ans

# print(solution([1, 2, 3, 9, 10, 12], 7))