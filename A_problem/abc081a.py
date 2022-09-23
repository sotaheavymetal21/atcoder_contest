# forを使う場合
S = input()  # 123を入力
N = [int(i) for i in list(S)]

count = 0
for i in N:
    if i == 1:
        count += 1

print(count)

# forを使わない場合 str型を使う
N = input()

counter = 0
if N[0] == "1":
    counter += 1
if N[1] == "1":
    counter += 1
if N[2] == "1":
    counter += 1

print(counter)
