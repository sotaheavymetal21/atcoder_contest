N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
A = set(A)

for i in range(N + 1):
    sota = True
    for j in A:
        if i == j:
            sota = False
    if sota == True:
        print(i)
        break
