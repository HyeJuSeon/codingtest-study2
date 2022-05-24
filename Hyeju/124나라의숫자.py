def solution(n):
    arr = ['1', '2', '4']
    ans = ''
    while n:
        n -= 1
        div, mod = divmod(n, 3)
        ans = arr[mod] + ans
        n = div
    return ans

# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
# print(solution(5))
# print(solution(6))
# print(solution(7))
# print(solution(8))
# print(solution(9))
# print(solution(10))

