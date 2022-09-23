N = int(input())
P = list(map(int, input().split()))

count = 0

for i in range(N-2):

    if min(P[i], P[i+1], P[i+2]) != P[i+1] and max(P[i], P[i+1], P[i+2]) != P[i+1]:
        count += 1
print(count)
