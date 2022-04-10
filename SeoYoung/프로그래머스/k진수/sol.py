# 양의 정수 n, k진수로 변환 시 변환 수 안에 조건에 맞는 소수가 몇개인지 카운트
# P 각 자릿수에 0을 포함하지 않는 소수
# 1. n을 k진수로 바꿔야 함
# 2. k진수로 바뀐 수가 제시된 3개의 형태에 맞는지 확인해야 함
import math

# n을 k진수로 변환하는 함수
def toKNumber(n,k):
    result=""
    while n!=0:
        result+=str(n%k)
        n=n//k    
    
    result=reversed(result)
    return ''.join(result)

# 소수 판별하는 함수
def isPrime(n):
    if n==1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer=0
    # 0을 기준으로 분리했을 때 ''을 제외한 모든 원소들은 기준에 부합함
    arr=toKNumber(n,k).split('0')
    
    # ''를 제외한 나머지 원소들 중 소수가 있으면 answer에 추가
    for i in arr:
        if len(i)==0: 
            continue
        if isPrime(int(i)): 
            answer+=1
    return answer