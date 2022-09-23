A, B, K = map(int, input().split())

asdf = []
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        asdf.append(i)

asdf = sorted(asdf, reverse=True)
print(asdf[K - 1])
