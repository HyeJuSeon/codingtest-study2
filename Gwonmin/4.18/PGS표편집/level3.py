#링크드 리스트
def solution(n, k, cmd):

    linked_list = {i: [i - 1, i + 1] for i in range(1, n+1)} #n=8일때 1~8까지
    OX = ["O" for i in range(1,n+1)]
    stack = []

    k += 1

    for c in cmd:
        c_lst = list(c.split())
        command = c_lst[0]
#현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
        if command == 'D':
            for _ in range(int(c_lst[1])):
                k = linked_list[k][1]
 #현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.         
        elif command == 'U':
            for _ in range(int(c_lst[1])):
                k = linked_list[k][0]

#현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        elif command == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k-1] = "X"

            if next == n+1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n+1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
#가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
        elif command == 'Z':
            prev, next, now = stack.pop()
            OX[now-1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n+1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(OX)


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))



'''
삽질
def solution(n, k, cmd):
    answer = ''
    #선택, 삭제, 복구
    print(n, k , cmd)
    pyo = []
    for i in range(n):
        if i == k:
            pyo.append(True)
        else:
            pyo.append(False)
    
    removed = []      
    for c in cmd:
        c_lst = list(c.split())
        command = c_lst[0]
        if command == 'U':
            num = int(c_lst[1])
            U(pyo,num)
        elif command == 'D':
            num = int(c_lst[1])
            D(pyo,num)
        elif command == 'C':
            C(pyo,removed)
        elif command == 'Z':
            Z(pyo,removed)
    
    for i in range(n):
        if i in removed:
            answer += "X"
        else:
            answer += "O"
    return answer
    
#현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
def U(pyo,num):
    selected_idx = pyo.index(True)
    pyo[selected_idx] = False
    pyo[selected_idx-num] = True
    return 

#현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
def D(pyo,num):
    selected_idx = pyo.index(True)
    pyo[selected_idx] = False
    pyo[selected_idx+num] = True
    return

#현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
def C(pyo,removed):
    selected_idx = pyo.index(True)
    pyo.pop(selected_idx)
    removed.append(selected_idx)
    if len(pyo) == selected_idx:
        selected_idx = len(pyo)-1
    pyo[selected_idx] = True
    return

#가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
def Z(pyo,removed):
    selected_idx = pyo.index(True)
    target_idx = removed.pop()
    pyo.insert(target_idx,False)
    if target_idx <= selected_idx:
        pyo[selected_idx] = False
        selected_idx += 1
        pyo[selected_idx] = True
    return

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
'''