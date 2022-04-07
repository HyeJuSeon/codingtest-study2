```
import sys

n = int(sys.stdin.readline())

stack = []
result = []

#불가능한 경우 False
temp = True

count = 1
for i in range(n):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        result.append('+')
        count+=1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in result:
        print(i)


#삽질
'''import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()
target = deque()
result = []

for i in range(n):
    target.append(int(sys.stdin.readline().strip()))

num = 1
while True:
    if num > n:
        break

    elif num <= target[0]:
        dq.append(num)
        result.append('+')
        num += 1

    elif dq[-1] == target[0]:
        dq.pop()
        target.popleft()
        result.append('-')

while dq:
    if dq.pop() != target.popleft():
        result = ['NO']
        break
    else:
        result.append('-')

for i in result:
    print(i)
  '''        
```
