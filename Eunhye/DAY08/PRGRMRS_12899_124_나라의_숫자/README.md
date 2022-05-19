## 풀이

기본적으로 3진수로 바꾸는것과 같지만 4를 사용해야하기 때문에 3으로 나누어 떨어질 때는 몫에 1을 더해주어 임의로 나머지를 만들어줍니다.

## 코드

```python
def solution(n):
    answer = ''
    while n != 0:
        quotient = n
        if n % 3 == 0:
            quotient = n // 3 - 1
            answer = '4' + answer
        else:
            quotient = n // 3
            answer = str(n % 3) + answer
        n = quotient
    return answer
```
