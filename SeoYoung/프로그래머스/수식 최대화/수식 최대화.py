import re
from itertools import permutations

def calculate(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2

def getResult(permu, exp):
    for p in permu:
        stack=[]
        while exp:
            temp=exp.pop(0)
            if temp==p:
                stack.append(calculate(stack.pop(),exp.pop(0),p))
            else:
                stack.append(temp)
        exp=stack
    return abs(exp[0])
    
def solution(expression):
    answer = 0
    exp=[]
    temp=""
    
    for i in expression:
        if i.isdigit()==True:
            temp+=i
        else:
            exp.append(int(temp))
            exp.append(i)
            temp=""
    exp.append(int(temp))
    
    op = [x for x in ['*', '+', '-'] if x in expression]
    result=[]
    for permu in permutations(op):
        temp=exp[:]
        result.append(getResult(permu, temp))
        
    return max(result)