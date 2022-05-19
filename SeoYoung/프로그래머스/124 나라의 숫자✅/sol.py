def solution(n):
    num=['4','1','2']
    answer = ""
    while n:
        answer=num[n%3]+answer
        if n%3==0:
            n=n//3-1
        else:
            n//=3
    return answer