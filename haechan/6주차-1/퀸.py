'''백준 - N-Queen

- 퀸 이동 방향: 일직선, 대각선
- 행과 열에 겹치게 놓이는 퀸은 없다
- 하나의 행에는 하나의 퀸만 놓일 수 있다
- 퀸이 4개라면, 리스트 안에 4개의 원소가 있는 상태이고
  각 리스트의 인덱스는 해당 퀸의 row를, 값은 해당 퀸의 column을 의미
  [1, 3, 0, 2] ==> 각 퀸의 위치는 (0, 1), (1, 3), (2, 0), (3, 2)
'''

def search(board, row):
    n = len(board)
    count = 0

    if n == row: # 마지막 행이라면 퀸을 하나만 놓을 수 있다
        return 1

    for col in range(n):
        board[row] = col # 각 행에 해당하는 컬럼 값 할당
        for i in range(row):
            if board[i] == board[row] or abs(board[i] - board[row]) == row - i: # 같은 열 검사, 대각 검사(행의 차와 열의 차 비교)
                break
        else:
            count += search(board, row + 1)

    return count

n = int(input())
print(search([0] * n, 0))