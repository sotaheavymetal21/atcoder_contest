# 自分の回答　不正解
# N = int(input())
# A = [input() for i in range(N)]
# S = sorted(A, key=int, reverse=True)
# print(S)
# count = 1

# for i in range(N-1):
#     if S[i] > S[i+1]:
#         print(i)
#         count += 1

# print(count)

N = int(input())
d = [int(input()) for _ in range(0, N)]

l = len(set(d))
print(d)
print(set(d))
print(l)

# if __name__ == '__main__':

#     # 入力
#     d = []
#     N = int(input())
#     for i in range(N):
#         d.append(int(input()))

#     # dのうち重複する要素を削除し、要素数を求める
#     num_d = len(list(set(d)))

#     # 出力
#     print(num_d)
