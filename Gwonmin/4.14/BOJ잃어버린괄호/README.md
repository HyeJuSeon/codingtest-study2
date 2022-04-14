
## 풀이

## 코드

```
#+연산만 괄호로 묶어주면 된다

line = input().split('-')
result = sum(map(int,line[0].split('+')))

for i in line[1:]:
    result -= sum(map(int,i.split('+')))

print(result)
```
