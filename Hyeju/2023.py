import math

N = int(input())
num = 10 ** N
def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def dfs(n):
    if len(str(n)) == N:
        print(n)
    else:
        for i in range(10):
            tmp = n * 10 + i
            if is_prime(tmp):
                dfs(tmp)
for p in [2, 3, 5, 7]:
    dfs(p)
