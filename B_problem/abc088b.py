N = int(input())
a = list(map(int, input().split()))
a_sort = sorted(a, reverse=True)

Alice = 0
Bob = 0

for i in range(N):
    if i % 2 == 0:
        Alice += a_sort[i]
    else:
        Bob += a_sort[i]

# Alice = sum(a[::2])
# Bob = sum(a[1::2]) これもいける。賢いやり方

print(Alice - Bob)
