def decimalToBinary(n):
    return "{0:b}".format(int(n))

def check(n, next_n):
    bi_n, bi_next_n = list(decimalToBinary(n)), list(decimalToBinary(next_n))
    n_ones, next_n_ones = len([i for i in bi_n if i == "1"]), len([j for j in bi_next_n if j == "1"])
    return n_ones == next_n_ones

def solution(n):
    for num in range(n+1, 1000001):
        if check(n, num):
            return num