from collections import deque

def solution(priorities, location):
    sequence = []
    dq = deque()

    for i in range(len(priorities)):
        temp_list = [-i, priorities[i]]
        dq.append(temp_list)

    while True:
        temp = dq.popleft()
        if len(dq) == 0:
            sequence.append(temp)
            break
        highest = max(map(max, dq))
        if temp[1] < highest:
            dq.append(temp)
        else:
            sequence.append(temp)

    answer = 0
    for i in sequence:
        answer += 1
        if -i[0] == location:
            return answer