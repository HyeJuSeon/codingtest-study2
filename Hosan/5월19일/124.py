def solution(n):
    dictionary= {1: 1, 2: 2, 0: 4}
    answer = ''
    while n:
        answer += str(dictionary[n % 3])
        if n % 3 :
            n = n//3
        else :
            n = n//3-1
    return answer[::-1]