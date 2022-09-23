S = input()

case = []
for i in range(len(S)):
    if (i+1) % 2 == 1:
        case.append(S[i])

print("".join(case))


# -----
S = input()
print(S[0::2])
