sent = input().split('-')
result = 0
for i in range(len(sent)) :
    tmp = sent[i].split('+')
    num_list = []
    for j in range(len(tmp)) :
        while tmp[j][0] == '0' :
            tmp[j] = tmp[j][1:]
        num_list.append(int(tmp[j]))
    value = sum(num_list)
    if i == 0 :
        result += value
    else :
        result -= value
print(result)

