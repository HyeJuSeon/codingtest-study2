import sys
from math import inf
from itertools import permutations

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split())) # + - * //
op_ = ['+', '-', '*', '//']
ops = []
for i in range(len(op)):
    ops.extend([op_[i] for _ in range(op[i])])

cases = list(permutations(ops))
max_ = -inf
min_ = inf
for case in cases:
    s = A[0]
    for i in range(1, N):
        if case[i - 1] == '+':
            s += A[i]
        elif case[i - 1] == '-':
            s -= A[i]
        elif case[i - 1] == '*':
            s *= A[i]
        else:
            s = int(s / A[i])
    max_ = max(max_, s)
    min_ = min(min_, s)
print(max_, min_, sep='\n')
