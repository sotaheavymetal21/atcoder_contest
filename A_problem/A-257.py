N, X = map(int, input().split())
apple = []

for i in range(N):
    for j in range(65, 91):
        apple.append(chr(j))
apple.sort()
print(apple[X - 1])
