def convert(n, k):
    if k == 10:
        return str(n)
    result = ""
    while n:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for div in range(2, int(n**(.5))+1):
        if n % div == 0:
            return False
    return True
    
def solution(n, k):
    converted = convert(n, k).split("0")
    prime = [ int(num) for num in converted if num and is_prime(int(num)) ]
    
    return len(prime)