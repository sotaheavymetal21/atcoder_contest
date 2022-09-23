N = int(input())
A = [[1]]

for i in range(1, N):
    asdf = [1]
    if i > 1:
        for j in range(1, i):
            asdf.append(A[i - 1][j - 1] + A[i - 1][j])
    asdf.append(1)
    A.append(asdf)

for i in A:
    print(*i)
