def solution(land):
    rows = land[0]
    for line in land[1:]:
        rows = [line[i] + max(rows[:i] + rows[i+1:]) for i in range(4)] # 이전 row의 i번째값을 제외한 max값을 현재 row의 i번째값에 합산

    return max(rows)