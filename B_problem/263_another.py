N = int(input())
P = [0, 0]+list(map(int, input().split()))
print(P)
attention = N  # いま注目している人
count = 0  # いま注目している人が人Nの何代前か
while attention != 1:
    # 1代遡る
    count += 1
    attention = P[attention]
print(attention)

print(count)
