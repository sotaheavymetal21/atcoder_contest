K = int(input())
A, B = map(str, input().split())

# int関数の2つ目の引数として整数を指定すると基数を指定できる
A = int(A, K)
B = int(B, K)

print(A, B)
volcano = A * B

print(volcano)
