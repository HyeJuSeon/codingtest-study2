'''백준 - 배열 복원하기

- (0,0)부터 (H-1, W-1)까지 범위에서 루프를 돌며 겹치는 부분 값 갱신
'''

H, W, X, Y = map(int, input().split())
B = []
for _ in range(H+X):
    B.append(list(map(int, input().split())))

tmp_A = [i[:W] for i in B[:H]] # B배열에서 A배열 크기만큼의 배열을 임시A 배열로 뺀다
for i in range(len(tmp_A)):
    for j in range(len(tmp_A[i])):
        if i >= X and j >= Y:
            tmp_A[i][j] = B[i][j] - tmp_A[i-X][j-Y]


for i in tmp_A:
    print(' '.join(map(str, i)))