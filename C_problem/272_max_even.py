N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

volcano = 0

for i in range(N-1):
    for j in range(i+1, N):
        if (A[i]+A[j]) % 2 == 0:
            if volcano < (A[i] + A[j]):
                volcano = (A[i] + A[j])

if volcano != 0:
    print(volcano)
else:
    print(-1)
