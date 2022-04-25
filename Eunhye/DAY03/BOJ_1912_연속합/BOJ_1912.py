N = int(input())
arr = list(map(int, input().split()))
cache = [0 for _ in range(N)]
cache[0] = arr[0]
for i in range(1, N):
    cache[i] = max(cache[i-1]+arr[i], arr[i])
print(max(cache))