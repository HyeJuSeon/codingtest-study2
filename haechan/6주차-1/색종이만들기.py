'''백준 - 색종이 만들기'''

import sys

def get_count(n, graph):
    global W_count, B_count
    # 현재 범위에서 전체가 0이거나, 전체가 1인지 확인
    # 전체가 0 혹은 1이라면, 재귀를 중단하고 count += 1
    if sum(sum(graph, [])) == 0:
        W_count += 1
        return
    elif sum(sum(graph, [])) == n*n:
        B_count += 1
        return

    # 더이상 자를 수 없는 경우 -> 중단
    if n / 2 < 1: return

    # (더 자를 수 있는 경우)0과 1이 섞여있으면, 4등분으로 나눈 범위를 다시 재귀로,
    n //= 2
    cutted_graph_up = graph[:n]
    cutted_graph_down = graph[n:]
    get_count(n, [arr[:n] for arr in cutted_graph_up]) # 왼쪽 위
    get_count(n, [arr[:n] for arr in cutted_graph_down]) # 왼쪽 아래
    get_count(n, [arr[n:] for arr in cutted_graph_up]) # 오른쪽 위
    get_count(n, [arr[n:] for arr in cutted_graph_down]) # 오른쪽 아래

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
global W_count, B_count
W_count = 0
B_count = 0

get_count(n, graph)

print(W_count)
print(B_count)