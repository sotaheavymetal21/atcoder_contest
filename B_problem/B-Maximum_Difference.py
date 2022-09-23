N = int(input())
A = list(map(int, input().split()))

S = sorted(A)
ans = 0
ans = abs(S[0] - S[-1])
print(ans)
