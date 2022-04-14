## 풀이

k진수로 바꾸어 준 n을 0을 기준으로 나눠주고, 소수의 개수를 세어주었습니다.

## 코드

```python
def convert(n, k):
    if k == 10:
        return str(n)
    result = ""
    while n:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for div in range(2, int(n**(.5))+1):
        if n % div == 0:
            return False
    return True

def solution(n, k):
    converted = convert(n, k).split("0")
    prime = [ int(num) for num in converted if num and is_prime(int(num)) ]

    return len(prime)
```
