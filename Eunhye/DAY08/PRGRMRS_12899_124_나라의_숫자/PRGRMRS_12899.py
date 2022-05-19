def solution(n):
    answer = ''
    while n != 0:
        quotient = n
        if n % 3 == 0:
            quotient = n // 3 - 1
            answer = '4' + answer
        else:
            quotient = n // 3
            answer = str(n % 3) + answer
        n = quotient
    return answer