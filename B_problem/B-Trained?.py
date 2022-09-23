N = int(input())
a = [int(input()) for _ in range(N)]

a.insert(0, 0)
print(a)  # [0, 3, 1, 2]

i = 1
for j in range(1, N + 1):
    i = a[i]

    if i == 2:
        print(j)
        break
else:
    print(-1)
