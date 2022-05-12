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

# temp=[0, 0, 2, 1] => operators=[2,2,3] 이런 식으로 넣어줌
for i in range(4):
    for j in range(temp[i]):
        operators.append(i)

max_val=-math.inf
min_val=math.inf

# operators의 순열을 구함
for permu in permutations(operators,n-1):
    # 해당 operator 순열로 계산한 결과값 val
    val=cal(operands, permu)

    # val을 현재 최댓값, 최솟값과 비교하여 갱신
    max_val=max(max_val, val)
    min_val=min(min_val, val)

print(max_val, min_val)