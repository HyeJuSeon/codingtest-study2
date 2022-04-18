## 풀이

## 코드

```python
from math import gcd
def solution(w,h):
    return w*h-(w+h-gcd(w,h))
```
