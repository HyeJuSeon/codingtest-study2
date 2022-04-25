'''프로그래머스 - 멀쩡한 사각형

- 수학문제..
- 전체 사각형 수 - (W + H - 최대공약수)
'''

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def solution(w, h):
    broken = w + h - gcd(w, h)
    return w * h - broken