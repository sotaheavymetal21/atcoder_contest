volcano = sorted(input())

if len(set(volcano)) == 2 and volcano[1] != volcano[2]:
    print("Yes")
else:
    print("No")
