S = input()

ACGT = ["A", "C", "G", "T"]

ans = 0
tmp = 0

for i in range(len(S)):
    if S[i] in ACGT:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0
print(ans)

S = input()

tmp = 0
ans = 0

for i in range(len(S)):
    if S[i] in "ACGT":
        tmp += 1
    else:
        tmp = 0
    result = max(result, tmp)
print(result)
