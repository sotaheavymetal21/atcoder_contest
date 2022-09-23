N = int(input())

flag = "No"
for i in range(N):
    for j in range(N):
        if j * 4 + i * 7 == N:
            flag = "Yes"

print(flag)
