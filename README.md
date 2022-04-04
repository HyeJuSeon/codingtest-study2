# 알고리즘 문제풀이

## 풀이 목록

|  #  |   날짜   | 문제이름 | 링크 | 풀이 | 완료 |  Best  |
| :-: | :------: | :-----: | :--: | :--: | :--: | :----: |
|  1  | 22-03-29 | 다단계 칫솔 판매 | [문제](https://programmers.co.kr/learn/courses/30/lessons/77486) | []() | ❌ | |

## Tips

- **2차원 배열 debugging 법**
  ```python
  arr = [[1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],]
  print(*arr, sep="\n") # 각각의 arr의 요소들을 "\n"로 구별하여 출력
  """
  [1, 2, 3, 4, 5]
  [1, 2, 3, 4, 5]
  [1, 2, 3, 4, 5]
  [1, 2, 3, 4, 5]
  [1, 2, 3, 4, 5]
  """
  ```

- **permutations & combinations**

  ```python
  from itertools import permutations, combinations
  items = [1, 2, 3, 4, 5]
  print(list(combinations(items, 2)))
  # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
  print(list(permutations(items, 2)))
  # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]
  ```

- **defaultdict**

  ```python
  from collections import defaultdict
  d_dict = defaultdict()
  d_dict[i] += 1 #초기화 없이 사용가능
  ```

- **Counter**

  ```python
  from collections import Counter
  items = [2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5] # Counter({5: 6, 1: 5, 3: 3, 2: 2, 4: 2})
  str1 = "eeeeelllllllllliiiiiccccccccee" # Counter({'l': 10, 'c': 8, 'e': 7, 'i': 5})
  cnt1 = Counter(items)
  cnt2 = Counter(str1)
  # 가장 많은 top 3
  cnt1.most_common(3) # [(5, 6), (1, 5), (3, 3)]
  cnt2.most_common(3) # [('l', 10), ('c', 8), ('e', 7)]
  ```

- **for-else, while-else 구문**

  ```python
  for or while:
     # 블라블라
     break
  else:
  # break를 통해 루프가 끝나지 않았을 경우에 쓰는 코드
  ```

- **import sys**

  - `sys.setrecursionlimit(limit_number)`
    - 재귀함수 제한 해제하고 싶을 때 ( default = 1000 )
  - `sys.stdin.readline()`
    - 입력 받을 때 ( input 보다 속도상에서 우위, 문자열로 입력받을 때 \n 개행까지 입력받으므로 주의 )

- **BFS: 큐를 이용 (from collections import deque)**
  - 최단거리 문제 (DFS보다 빠를때가 많음)
- **DFS: 스택를 이용 (python list 사용)**
  - 백트래킹 문제 (모든 경우의 수를 봐야할 때)
