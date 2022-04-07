n = int(input())
count = 0
stack = []
result = []
flag = True
for i in range(0,n):
    x = int(input())
    while count < x:
      count += 1
      stack.append(count)
      result.append("+")
    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break
if flag == False:
    print("NO")
else:
    print("\n".join(result))