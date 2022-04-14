import sys
input = sys.stdin.readline
N = int(input())
for i in range(N) :
    num_p = int(input())
    candidate = []
    count = 1
    for j in range(num_p) :
        sc1, sc2 = map(int, input().split())
        candidate.append((sc1, sc2))
    candidate.sort()
    Max = candidate[0][1]
    for j in range(1, len(candidate)) :
        if Max > candidate[j][1] :
            count += 1
            Max = candidate[j][1]
    print(count)

