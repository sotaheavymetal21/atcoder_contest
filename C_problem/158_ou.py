A, B = map(int, input().split())

exist = False

for i in range(1, 10001, 1):
    if i * 0.08 // 1 == A and i * 0.1 // 1 == B:
        exist = True
        break

print(i if exist else '-1')
