N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for i in range(N + 1)]
dp[0][0] = 1
mod = 998244353

for i in range(1, N + 1):
    for j in range(K + 1):
        for l in range(1, M + 1):
            if l + j <= K:
                dp[i][j + l] += dp[i - 1][j]

print(sum(dp[N]) % mod)
