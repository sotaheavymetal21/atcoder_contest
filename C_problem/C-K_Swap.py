N, K = map(int, input().split())
a = list(map(int, input().split()))

tmp = 0
count = 0

b = sorted(a)
while a != b:
    for i in range(N - K):
        if a[i] > a[i + K]:
            tmp = a[i]
            a[i] = a[i + K]
            a[i + K] = tmp
            count += 1
    if count == 0:
        break
    count = 0

if a == b:
    print("Yes")
else:
    print("No")
