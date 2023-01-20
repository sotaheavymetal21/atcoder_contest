A, B, C = map(int, input().split())

for i in range(1, 10):
    multiple_C = C * i
    if A <= multiple_C <= B:
        print(multiple_C)
        break
    if multiple_C > B:
        print(-1)
        break
