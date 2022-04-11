def solution(n, left, right):
    ans = []
    for i in range(int(left), int(right) + 1):
        ans.append(max(divmod(i, n)) + 1)
    return ans

# print(solution(3, 2, 5))
# print(solution(4, 7, 14))