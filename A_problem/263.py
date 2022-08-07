hull_house = list(map(int, input().split()))

hull_house = sorted(hull_house)

if (hull_house[1] != hull_house[2] or hull_house[2] != hull_house[3]) and len(set(hull_house)) == 2:
    print("Yes")
else:
    print("No")
