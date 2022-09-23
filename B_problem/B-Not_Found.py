S = input()

a_to_z = "abcdefghijklmnopqrstuvwxyz"
ans = "None"

for i in a_to_z:
    if i in S:
        continue
    else:
        ans = i
        break
print(ans)
