N, K = map(int, input().split())
A = list(map(int, input().split()))
XY = [map(float, input().split()) for _ in range(N)]
X, Y = [list(i) for i in zip(*XY)]

# この問題の答えは、全ての人について、""その人から最も近い『明かりを持った人』""までの距離の最大値となります。

rock = 100000000000000
metal = 0
ans = []
for j in range(N):
    for k in range(K):
        metal = ((X[j] - X[A[k] - 1]) ** 2) + ((Y[j] - Y[A[k] - 1]) ** 2)


print(max(ans) ** 0.5)
