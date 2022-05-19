N = int(input())
col = set()
pos_diag = set() # r + c
neg_diag = set() # r - c

result = 0
def backtrack(r):
    global result
    if r == N:
        result += 1
        return
    for c in range(N):
        if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
            continue
        
        col.add(c)
        pos_diag.add(r+c)
        neg_diag.add(r-c)
        
        backtrack(r+1)
        
        col.remove(c)
        pos_diag.remove(r+c)
        neg_diag.remove(r-c)
        
backtrack(0)
print(result)