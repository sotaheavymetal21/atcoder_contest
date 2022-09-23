# N = int(input())

# magnitude = 0
# counter = 0
# flag = True

# for i in range(1, N+1):
#     if i % 2 == 0:
#         if i % 2 == 1:
#             print(i)
#             flag = False
#             magnitude += 1
#             magnitude = max(magnitude, counter)
#             break
#         else:
#             print(f"elseに入った{i}")
#             i = i // 2
#             counter += 1
# print(magnitude)

N = int(input())

ans = 1
while ans < N:
    if ans*2 <= N:
        ans *= 2
    else:
        break

print(ans)

N = int(input())
i = 1
while i * 2 <= N:
    i *= 2
print(i)

N = int(input())

A = []

for i in range(1, N + 1):
    for j in range(N + 1):
        if i % 2 ** j == 0:
            A.append(2 ** j)
print(max(A))
