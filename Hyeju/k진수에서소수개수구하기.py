def solution(n, k):
    s = ''
    while n:
        s += str(n % k)
        n = n // k
    s = s[::-1]
    li = s.split('0')
    li = [int(l) for l in li if l != '']

    ans = 0
    for l in li:
        is_prime = True
        if l < 2:
            continue
        for i in range(2, int(l ** 0.5) + 1):
            if l % i == 0:
                is_prime = False
                break
        if is_prime:
            ans += 1
    return ans

# print(solution(437674, 3))
# print(solution(110011, 10))