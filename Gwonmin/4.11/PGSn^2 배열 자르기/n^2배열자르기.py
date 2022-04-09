# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.

#무지성 시간초과 2중 for문 없애야함
'''
def solution(n, left, right):
    answer = []
    # arr = [[0 for i in range(n)] for i in range(n)]
    idx = 0 
    for i in range(n):
        for j in range(n):
            if idx > right:
                break
            if idx >= left and idx <= right:
                answer.append(i+1 if i >= j else j+1)
            idx += 1
            
    # for i in arr:
    #     answer += i

    return answer
'''
import math
#좌표로 접근해야한다
def solution(n, left, right):
    answer = []

    #left, right int()로 감싸줘야 런타임에러 안나는데 왜 그런지 모르겠다
    for num in range(int(left),int(right)+1):
        row = math.floor(num/n)
        col = num % n
        max_num = row+1 if row > col else col+1
        answer.append(max_num)
    return answer


print(solution(3,2,5))