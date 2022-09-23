N, x = map(int, input().split())
a = list(map(int, input().split()))

count = 0
a = sorted(a)
print(a)
print(len(a))
for i in range(len(a)):
    if x < a[i]:
        break
    else:
        x -= a[i]
        count += 1

    if i == len(a) - 1 and x > 0:
        count -= 1

print(count)
