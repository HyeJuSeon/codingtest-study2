formula=input()
nums=[list(map(int,i.split('+'))) for i in formula.split('-')]
answer=sum(nums[0])

for i in range(1, len(nums)):
    answer-=sum(nums[i])

print(answer)



