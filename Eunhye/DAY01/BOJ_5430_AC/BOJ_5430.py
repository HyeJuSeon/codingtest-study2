from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  p = input()
  n = int(input())
  arr = input().rstrip().replace("[", "").replace("]","")
  arr = arr.split(",") if arr else []
  arr = deque(arr)
  result = ""
  start_idx = 0
  end_idx = 1
  reversed = 0
  while end_idx <= len(p):
    if end_idx < len(p) and p[start_idx] == p[end_idx]:
      end_idx += 1
    else:
      func_num = end_idx - start_idx
      if p[start_idx] == "R" and func_num % 2:
        reversed = 0 if reversed else 1
      elif p[start_idx] == "D":
        if func_num > len(arr):
          result = "error"
          break
        else:
          for _ in range(func_num):
            if reversed:
              arr.pop()
            else:
              arr.popleft()
          # arr = arr[:len(arr)-func_num] if reversed else arr[func_num:] 
      start_idx = end_idx
      end_idx = start_idx+1
  else:
    if reversed:
      arr.reverse()
    result = "[" + ",".join(arr) + "]"
  print(result)
