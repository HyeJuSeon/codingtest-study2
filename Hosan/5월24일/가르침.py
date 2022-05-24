import sys
from itertools import combinations
from string import ascii_lowercase
input = sys.stdin.readline

N, K = map(int, input().split())
K = K - 5
alphabet_list = list(set(list(ascii_lowercase)) - set(['a', 'c', 'n', 't', 'i']))
word_list = []
for i in range(N) :
    tmp = input()
    tmp = tmp[4:-5]
    word_list.append(tmp)
count = 0
if K < 0 :
    print(0)
else :
    for alphabet in combinations(alphabet_list, K) :
        alphabet = list(set(alphabet) | set(['a', 'c', 'n', 't', 'i']))
        tmp_count = 0
        for i in range(N) :
            flag = True
            tmp = word_list[i]
            for j in tmp :
                if j not in alphabet :
                    flag= False
                    break
            if flag :
                tmp_count += 1
        if tmp_count > count :
            count = tmp_count
    print(count)
