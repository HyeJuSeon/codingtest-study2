## 풀이

패턴을 찾아 처리해주었습니다.
해당 row에 따른 row_lst는 다음과 같습니다.

```
row_lst = [row]*row + [i for i in range(row+1, n+1)]
```

가장 처음과 마지막은 예외처리를 해주고 나머지 반복되는 부분은 반복문을 돌려 처리해주었습니다.

## 코드

```python
def solution(n, left, right):
    answer = []
    # 테스트케이스 12, 13 아마 left와 right가 long이라서 그런듯
    left = int(left)
    right = int(right)

    # 제일 첫 row 처리
    row = (left // n)+1
    col = left % n
    row_lst = [row]*row + [i for i in range(row+1, n+1)]
    answer.extend(row_lst[col:])
    left += n-col

    # 반복되는 부분 처리
    for i in range(left, right+1, n):
        row = (i // n)+1
        col = i % n
        row_lst = [row]*row + [j for j in range(row+1, n+1)]
        answer.extend(row_lst)

    # 제일 마지막 row에서 제외해줄 수의 개수
    exclude = n - (right % n + 1)
    return answer[:len(answer)-exclude]
```
