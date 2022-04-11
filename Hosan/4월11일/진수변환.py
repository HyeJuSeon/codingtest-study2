def convert(n, q) :
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def getPrimeNum(n):
    if n == 1 :
        return False
    elif n == 2 :
        return True
    m = int(n ** 0.5) + 1
    for i in range(2, m):
        if n % i == 0 :
            return False
    return True

def solution(n, k):
    n = convert(n, k)
    List =  str(n).split('0')
    List = list(filter(lambda x: x != '', List))
    List = list(map(lambda x: getPrimeNum(int(x)), List))
    return List.count(True)