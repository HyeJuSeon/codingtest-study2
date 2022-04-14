import sys
#DP문제

n = int(input())
num_list = list((map(int,sys.stdin.readline().strip().split())))

for i in range(1,n):
    num_list[i] = max(num_list[i],num_list[i]+num_list[i-1])

print(max(num_list))