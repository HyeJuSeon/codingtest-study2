'''백준 1874 - 스택수열'''

n = int(input())

result = []
stack = []
push_cnt = 1 # 추가해준 숫자 개수 ==> 스택에 마지막으로 추가한 숫자
for i in range(n):
    input_num = int(input())
    while push_cnt <= input_num: # push_cnt와 현재 수열의 수와 같아질때까지 연산 추가(그래야 input_num을 스택에서 뺼 수 있으니까)
        stack.append(push_cnt)
        result.append("+")
        push_cnt += 1
    if input_num == stack[-1]:
        stack.pop()
        result.append("-")

if stack != []: # 연산을 다 마쳤는데 스택이 비어있지 않다면 불가능한 수열
    print("NO")
else:
    for s in result:
        print(s)