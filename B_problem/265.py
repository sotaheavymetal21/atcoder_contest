N, M, T = map(int, input().split())
A = list(map(int, input().split()))
X = []
for i in range(M):
    X.append(list(map(int, input().split())))

flag = False

for i in range(N-1):
    T = T - A[i]

if M > 0:
    for j in range(M):
        T += X[j][1]

if T > 0:
    flag = True

if flag:
    print("Yes")
else:
    print("No")
