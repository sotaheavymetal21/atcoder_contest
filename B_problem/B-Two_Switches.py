A, B, C, D = map(int, input().split())

ans = 0

if A > C:
    A, B, C, D = C, D, A, B

if B < C:
    ans = 0
elif D < B:
    ans = D - C
else:
    ans = B - C

print(ans)

start = max(A, C)
end = min(B, D)
print(max(0, end - start))
