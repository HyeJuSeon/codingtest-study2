size = int(input())
data = list(map(int, input().split()))
data2 = []
for i in range(len(data)) :
    data2.append([data[i], data[i]])
for i in range(1, size) :
    a = data2[i-1][0]
    b = data2[i-1][1]
    data2[i][0] = max(a, b) + data2[i][0]
print(max(map(max, data2)))
