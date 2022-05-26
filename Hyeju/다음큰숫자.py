def solution(n):
    cnt = format(n, 'b').count('1')
    while 1:
        n += 1
        if cnt == format(n, 'b').count('1'):
            return n

# print(solution(78))
# print(solution(15))