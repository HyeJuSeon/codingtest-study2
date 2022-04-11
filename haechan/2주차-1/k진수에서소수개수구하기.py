'''프로그래머스 - k진수에서 소수개수 구하기

- 1번 시간초과 문제 : is_prime 함수
    ==> 제곱수의 왼쪽값들에 대해서만 판별하면 오른쪽을 판별한것과 같다. 연산을 1/2로 줄일 수 있다.
    ==> n=16이라면 약수는 1, 2, 4, 8, 16 이고 중간값인 4를 기준으로 왼쪽 오른쪽의 약수가 대칭된다
    ==> 즉 중간값을 기준으로 왼쪽 혹은 오른쪽 중 한쪽만 약수가 있는지 확인하면 된다
'''

import math

# 진수 변환 함수: 변환하고자 하는 수 n을 바꾸고자 하는 진수 k로 
# 나눌수 없을 때까지 나눈 뒤 남은 몫과 나머지를 반대 방향으로 읽는다
def trans_n(n, q):
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def is_prime(num):
    # num의 제곱근(약수의 중간값)의 왼편에 약수가 없다면 오른편에도 없다
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
        