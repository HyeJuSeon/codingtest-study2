def solution(n):
    temp = ['1','2','4']
    answer = ''

    while True:
        if n%3 == 1:
            answer += temp[0]
        elif n%3 == 2:
            answer += temp[1]
        elif n%3 == 0:
            answer += temp[2]

        if n <= 3:
            break

        if n%3 == 0:
            n = n//3 - 1
        else:
            n = n//3
    return answer[::-1]

