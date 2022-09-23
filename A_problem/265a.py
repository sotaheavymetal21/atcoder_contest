X, Y, N = map(int, input().split())

if N >= 3:
    apple = N // 3
    orange = N - (apple * 3)
    money = min((apple * Y) + (orange * X), (N * X))
    print(money)
else:
    print(X * N)
