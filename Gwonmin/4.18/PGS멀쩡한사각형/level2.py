import math
#최대공약수 풀이
#수학
def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))

'''
def solution(w,h):
    answer = 0
    #한 칼럼당 몇개의 정사각형을 뺴야하는지 찾기
    if h >= w:
        gradient = h/w
        remove_box = math.ceil(gradient)
        answer = w*h - remove_box * w
    else:
        gradient = abs(w/h)
        remove_box = math.ceil(gradient)
        answer = w*h - remove_box * h
    return answer
'''