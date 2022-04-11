'''프로그래머스 - n**2 배열 자르기

- 각 좌표 (x, y)의 값은 max(x, y) + 1과 같다는 규칙
'''

def solution(n, left, right):
    result = []
    for i in range(int(left), int(right)+1):
        q, r = divmod(i, n) # 몫과 나머지 | 구하고자하는 인덱스에서 n으로 나눈 몫(행)과 나머지(열)가 해당 행렬에서의 좌표
        result.append(max(q, r) + 1)

    return result