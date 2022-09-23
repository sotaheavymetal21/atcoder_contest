N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range(N):
    if A[i] == B[i]:
        count += 1

year = - count

# for i in range(N):
#     for j in range(N):
#         if A[i] == B[j]:
#             year += 1

for i in range(N):
    if A[i] in B:
        year += 1
        print(f"やほー{i}")
print(count)
print(year)
