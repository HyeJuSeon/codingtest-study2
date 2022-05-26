def toBinary(n):
    answer=[]
    while n:
        answer.append(n%2)
        n//=2
    return answer


def solution(n):
    cnt=toBinary(n).count(1)
    for answer in range(n+1, 1000001):
        if cnt==toBinary(answer).count(1):
            return answer