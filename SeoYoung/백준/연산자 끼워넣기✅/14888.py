from itertools import permutations
import math

def cal(nums, opers):
    idx=1
    result=nums[0]
    
    for oper in opers:
        if oper==0:
            result+=nums[idx]
        elif oper==1:
            result-=nums[idx]
        elif oper==2:
            result*=nums[idx]
        elif oper==3:
            result=int(result/nums[idx])
        idx+=1
    
    return result
    

n=int(input())
operands=list(map(int,input().split()))
temp=list(map(int,input().split()))
operators=[]

for i in range(4):
    for j in range(temp[i]):
        operators.append(i)

max_val=-math.inf
min_val=math.inf

for permu in permutations(operators,n-1):
    val=cal(operands, permu)

    max_val=max(max_val, val)
    min_val=min(min_val, val)

print(max_val, min_val)