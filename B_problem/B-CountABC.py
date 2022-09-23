N = int(input())
S = list(input())

count = 0
for i in range(N-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        count += 1
print(count)


# なぜだめなのかわからない。
ans = 0
for i in range(N-2):
    if S[i:i+3] == 'ABC':
        ans += 1

print(ans)
