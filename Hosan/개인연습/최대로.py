from itertools import permutations

size = int(input())
arr = list(input().split())
add, mul = map(int, input().split())
result = 0

def evaluate(value) :
    tmp = value.split("*")
    result = 1
    for i in tmp :
        result *= eval(i)
    return result

def dfs(arr, add, mul, depth, value) :
    global result
    if mul == 0 and add == 0:
        a = evaluate(value)
        result = max(a, result)
    else :
        if mul > 0 :
            tmp = value
            value = value + "*" + arr[depth]
            dfs(arr, add, mul-1, depth + 1, value)
            value = tmp
        if add > 0 :
            value = value + "+" + arr[depth]
            dfs(arr, add-1, mul, depth + 1, value)

for perm in permutations(arr) :
    dfs(perm, add, mul, 1, perm[0])
print(result)