## 풀이

## 코드

```python
N, K = map(int, input().split())
words = []
result = 0
learned = [0 for _ in range(26)]

for ch in "acint":
    learned[ord(ch)-ord("a")] = 1

def backtrack(idx, k_cnt):
    global words, result, K
    if k_cnt == K:
        cnt = 0
        for word in words:
            for w in word:
                if not learned[ord(w)-ord("a")]:
                    break
            else: cnt += 1
        result = max(result, cnt)
        return

    for i in range(idx, 26):
        if not learned[i]:
            learned[i] = 1
            backtrack(i, k_cnt+1)
            learned[i] = 0

for _ in range(N):
    input_word = input()
    words.append(set(input_word[4:-4]))

if K >= 5:
    backtrack(0, 5)
    print(result)
else: print(0)

```
