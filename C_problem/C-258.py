# from collections import deque

# N, Q = map(int, input().split())
# S = list(input())
# S = deque(S)
# Query = [list(map(int, input().split())) for i in range(Q)]

# for i in range(Q):
#     if Query[i][0] == 2:
#         print(S[Query[i][1] - 1])
#         continue
#     if Query[i][0] == 1:
#         S.rotate(Query[i][1])

# def main():
#     n, q = map(int, input().split())
#     s = input()

#     rot = 0
#     for _ in range(q):
#         t, x = map(int, input().split())

#         if t == 1:
#             rot += x
#         else:
#             print(s[(x - rot) % n - 1])


# if __name__ == "__main__":
#     main()

N, Q = map(int, input().split())
S = input()
P = 0

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        P += x
    else:
        y = (x - 1 - P) % N
        print(S[y])
