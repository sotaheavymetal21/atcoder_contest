N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1):
        if (10000 * i + 5000 * j + 1000 * (N - (i + j)) == Y) & (0 <= (N - (i + j)) <= N):
            print(i, j, N - (i + j))
            exit()
print(-1, -1, -1)
