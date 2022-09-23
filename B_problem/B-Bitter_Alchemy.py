N, X = map(int, input().split())
M = []

for i in range(N):
    M.append(int(input()))

sum = 0
surplus = 0

for j in range(N):
    sum += M[j]

surplus = (X - sum) // min(M)
print(len(M) + surplus)

# -----------
N, X = map(int, input().split())
num_list = [int(input()) for k in range(N)]
X = X - sum(num_list)
ans = X // min(num_list)
print(N + ans)

# -----------
a, b = [int(x) for x in input().split()]
c = []
for _ in range(a):
    c.append(int(input()))
print(len(c)+(b-sum(c))//min(c))
