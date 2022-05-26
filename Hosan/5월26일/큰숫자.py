def solution(n) :
    answer = 0
    count = bin(n).count("1")
    for i in range(n+1, 1000001) :
        tmp = bin(i).count("1")
        if count == tmp :
            answer = i
            break
    return answer