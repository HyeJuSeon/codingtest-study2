N=int(input())
stack=[]
answer=[]
count=1
not_return=False

for i in range(N):
    num=int(input())
    
    while count<=num:
        stack.append(count)
        answer.append('+')
        count+=1
    
    if stack[-1]==num:
        stack.pop()
        answer.append('-')
    
    elif stack[-1]>num:
        not_return=True
        break

if not_return:
    print("NO")
else:
    print("\n".join(answer))


    