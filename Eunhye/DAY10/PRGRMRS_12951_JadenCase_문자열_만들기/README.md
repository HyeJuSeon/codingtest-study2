## 풀이

한 개의 공백 단위로 split해 준 뒤(공백 문자가 연속해서 나올 수 있기 때문) 단어들의 첫 글자를 대문자화해주는 capitalize를 사용하였습니다.

## 코드

```python
def solution(s):
    return " ".join([word.capitalize() for word in s.lower().split(" ")])
```
