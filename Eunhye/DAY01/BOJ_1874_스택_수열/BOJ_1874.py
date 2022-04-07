n = int(input())
stack = []
result = []
elem_num = 1
flag = 0
for _ in range(n):
  curr_num = int(input())
  if not stack:
    stack.append(elem_num)
    elem_num += 1
    result.append("+")
  # 스택의 마지막 요소가 curr_num이랑 같지 않을 때
  while stack and stack[-1] != curr_num:
    if curr_num > stack[-1]: # curr_num이 클 때는 숫자를 더 append
      stack.append(elem_num)
      elem_num += 1
      result.append("+")
    elif curr_num < stack[-1]: # curr_num이 더 작을 때는 만들 수 없는 수열
      flag = 1
      break
  if stack and stack[-1] == curr_num: # curr_num이랑 같을 때는 pop
    stack.pop()
    result.append("-")

if flag:
  print("NO")
else:
  print(*result, sep="\n")
