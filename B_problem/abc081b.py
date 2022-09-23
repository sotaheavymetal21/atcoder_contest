N = int(input())
A = list(map(int, input().split()))

counter = 0
flag = True

while flag == True:
    for i in range(N):
        if A[i] % 2 == 1:
            print(counter)
            flag = False
            break
        else:
            A[i] = A[i] / 2
counter += 1


# A = list(map(int, input().split()))
# length = len(A)

# flag = True
# count = 0

# while flag == True:
#     for i in range(length):
#         if not A[i] % 2 == 0:
#             print(count)
#             flag = False
#             break
#         else:
#             A[i] = A[i] / 2
#     count += 1
