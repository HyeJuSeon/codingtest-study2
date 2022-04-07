## 백준 1874 스택 수열

### 알고리즘

```txt
 ✅ 스택 자료구조 사용
```

### 코드 구현

사용 언어 : **파이썬**

```python
N=int(input())
stack=[]
answer=[]
# 현재 스택에 몇번째 숫자까지 넣었는지 체크하는 변수 count
count=1
# 입력된 수열을 리턴하지 못할 경우를 체크
not_return=False

for i in range(N):
    num=int(input())

    # 입력받은 숫자보다 count가 작으면 스택에 count=num될 때까지 계속 넣어줌
    # push 연산할 때마다 answer에 + 도 넣어줌
    while count<=num:
        stack.append(count)
        answer.append('+')
        count+=1

    # 스택 top 값이 num이면 pop
    if stack[-1]==num:
        stack.pop()
        answer.append('-')

    # 스택 top값이 num보다 크다는 것은 해당 수열을 만들 수 없다는 뜻이므로
    # not_return을 True로 바꿔준 후 for문 빠져나감
    elif stack[-1]>num:
        not_return=True
        break

if not_return:
    print("NO")
else:
    print("\n".join(answer))

```
