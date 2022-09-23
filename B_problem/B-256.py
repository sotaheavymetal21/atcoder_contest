N = int(input())
A = list(map(int, input().split()))

sota = []
asdf = []

for i in range(N):
    for j in range(i + 1, N):
        A[i] += A[j]
    sota.append(A[i])

for k in range(len(sota)):
    if sota[k] >= 4:
        asdf.append(sota[k])
print(len(asdf))
