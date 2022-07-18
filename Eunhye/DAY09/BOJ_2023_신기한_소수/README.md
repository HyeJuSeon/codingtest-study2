## 풀이

backtracking으로 풀었습니다.

우선 숫자가 소수가 되려면 가장 앞에 오는 숫자는 소수가 되어야 합니다. 그래서 first에 1부터 9까지의 수 중 소수인 2, 3, 5, 7을 넣어줍니다.  

그 뒤로 오는 숫자는 소수가 아니어도, 홀수면 가능합니다. 짝수는 2를 약수로 가지게 되므로 될 수 없습니다. others 홀수인 1, 3, 5, 7, 9를 넣어줍니다.  

이후로는 N개만큼 숫자를 늘려주며 늘려주어 만든 숫자가 소수일 경우에만 backtrack을 돌려줍니다. N자리 수가 만들어지면 result에 해당 숫자를 넣어줍니다.  

마지막에는 result를 정렬해준 뒤 출력해줍니다.  

## 코드

```python
N = int(input())

# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

first = [2, 3, 5, 7]
others = [1, 3, 5, 7, 9]
result = []
def backtrack(n, depth):
    global result
    if depth == N:
        result.append(n)
        return
    for num in others:
        if is_prime(n*10+num):
            backtrack(n*10+num, depth+1)

for f in first:
    backtrack(f, 1)

print(*sorted(result), sep="\n")
```
