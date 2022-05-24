N = int(input())

# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

first = [2, 3, 5, 7]
others = [1, 3, 5, 7, 9]
result = []
def backtrack(n, depth):
    global result
    if depth == N:
        result.append(n)
        return
    for num in others:
        if is_prime(n*10+num):
            backtrack(n*10+num, depth+1)

for f in first:
    backtrack(f, 1)

print(*sorted(result), sep="\n")