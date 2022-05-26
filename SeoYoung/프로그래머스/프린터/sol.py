def solution(priorities, location):
    answer = 0
    stack=[]
    for i in range(len(priorities)):
        stack.append((priorities[i],i))
    priorities.sort(reverse=True)
    
    while True:
        if stack[0][0]==priorities[0]:
            answer+=1
            if stack[0][1]==location:
                break
            stack.pop(0)
            priorities.pop(0)
        else:
            p=stack.pop(0)
            stack.append(p)
    
    return answer