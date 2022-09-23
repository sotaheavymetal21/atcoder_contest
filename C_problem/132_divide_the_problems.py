# 回答１、無駄ループでTLE&WA
N = int(input())
D = list(map(int, input().split()))
D_sort = sorted(D)

count = 0
if D_sort[:N // 2][-1]+1 == D_sort[N // 2:][1]:
    print(count)
    exit()

for i in range(D_sort[:N // 2][-1]+1, D_sort[N // 2:][0]+1):
    if D_sort[:N // 2][-1] < i <= D_sort[N // 2:][1]:
        count += 1
print(count)

# abs関数の偉大さ
N = int(input())
D = list(map(int, input().split()))
D_sort = sorted(D)

print(abs(D_sort[N // 2 - 1] - D_sort[N // 2]))
