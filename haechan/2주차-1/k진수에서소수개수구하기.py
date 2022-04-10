'''프로그래머스 - k진수에서 소수개수 구하기

- 1번 시간초과 ==> 특정 수 N의 약수들을 일렬로 나열했을 때 그 중 가운데의 수를 중심으로 약수가 대칭 
            ==> 제곱수의 왼쪽값들에 대해서만 판별하면 오른쪽을 판별한것과 같다. 연산을 1/2로 줄일 수 있다.
'''

import math

def trans_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True
            
def solution(n, k):
    num = trans_n(n, k)
    num_list = num.split("0")
    
    prime_cnt = 0
    for nums in num_list:
        if nums != "" and int(nums) != 1:
            if is_prime(int(nums)):
                prime_cnt += 1
            
    return prime_cnt
        