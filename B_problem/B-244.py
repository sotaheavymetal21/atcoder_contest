N = int(input())
T = list(input())

count = 0
x = 0
y = 0

for i in T:
    if i == "R":
        count += 1
    elif i == "S":
        if count % 4 == 0:
            x += 1
        elif count % 4 == 1:
            y -= 1
        elif count % 4 == 3:
            y += 1
        elif count % 4 == 2:
            x -= 1

print(x, y)

# N = int(input())
# T = list(input())
# A = [1, 0]
# X = [0, 0]
# for i in range(N):
#     if T[i] == "S":
#         X[0] += A[0]
#         X[1] += A[1]
#     elif T[i] == "R":
#         A[0], A[1] = A[1], -1 * A[0]
# print(X[0], X[1])
