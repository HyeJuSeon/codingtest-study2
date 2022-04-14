'''백준 - 신입사원

- 오름차순 정렬
- 가장 앞에 있는 지원자의 성적순위를 기준으로 모든 지원자의 성적순위와 비교

[(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]
[(1, 4), (2, 5), (3, 6), (4, 2), (5, 7), (6, 1), (7, 3)]

- 맨 앞 사람은 서류심사 순위를 기준으로 1위이므로 무조건 채용
- 맨 앞 사람과 면접심사 순위를 순차적으로 비교 -> 다하면 시간초과..
- 맨 앞 사람하고만 한번씩 비교했을 때 살아남은 사람들을 리스트에 넣어 그 사람들끼리만 다시 비교
'''
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    record_list = []
    for _ in range(N):
        r_rank, i_rank = map(int, input().split())
        record_list.append((r_rank, i_rank))

    record_list.sort() # 서류점수 순위 순으로 오름차순 정렬
    top_rank = record_list[0][1] # 서류점수 1등의 면접점수

    fail_cnt = 0
    failed_list = []
    for i in range(1, N):
        _, i_rank = record_list[i]
        if i_rank > top_rank:
            failed_list.append(record_list[i])
            fail_cnt += 1
        else: # 순위가 더 높은 사람이 있으면 그 사람의 순위로 top_rank 갱신
            top_rank = i_rank

    print(N - fail_cnt)