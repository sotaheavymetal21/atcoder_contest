H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

mine = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            mine += 1
            S[i][j - 1] = str(mine)
            S[i][j + 1] = str(mine)
            S[i - 1][j] = str(mine)
            S[i + 1][j] = str(mine)
            S[i - 1][j - 1] = str(mine)
            S[i - 1][j + 1] = str(mine)
            S[i + 1][j + 1] = str(mine)
            S[i + 1][j - 1] = str(mine)

for k in range(H):
    print("".join(S[k]))
# ちょっとできなかったのでまた時間を置いて挑戦します。
