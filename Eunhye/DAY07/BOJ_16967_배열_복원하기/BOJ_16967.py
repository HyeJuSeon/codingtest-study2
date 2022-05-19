H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H+X)]
A = [ B[b][:W] for b in range(H)]

for i in range(X,H):
  for j in range(Y,W):
    A[i][j] -= A[i][j] - B[i+X][j+Y]

for k in range(H):
  print(*A[k], sep=" ")

