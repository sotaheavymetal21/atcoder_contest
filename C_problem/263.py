import itertools

N, M = map(int, input().split())

asdf = []
for i in range(1, M+1):
    asdf.append(i)

for i in itertools.combinations(asdf, N):
    print(*i)
