# 272 A Integer Sum

N = int(input())
A = list(map(int, input().split()))

volcano = 0

for i in range(N):
    volcano += A[i]
print(volcano)
