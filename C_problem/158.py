A, B = map(int, input().split())

for giant_kingdom in range(1, 1251):
    if int(giant_kingdom * 0.08) == A and int(giant_kingdom * 0.10) == B:
        volcano = giant_kingdom
        print(volcano)
        exit()

print("-1")
