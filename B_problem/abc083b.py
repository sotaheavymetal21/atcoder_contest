N, A, B = map(int, input().split())

counter = 0

for i in range(N + 1):
    n = 0
    for j in list(str(i)):
        print("iを出力")
        print(i)  # 20 <class 'int'>

        print("str(i)を出力")
        print(str(i))  # 20 <class 'str'>

        print("list(str(i))を出力")
        print(list(str(i)))  # ["2", "0"]

        print(int(j))  # 2, 0
        n += int(j)

    if A <= n <= B:
        counter += i

print(counter)

N, A, B = map(int, input().split())

counter = 0
for i in range(1, N + 1):
    n = i // 10000 + i % 10000 // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10
    if A <= n <= B:
        counter += i

print(counter)
