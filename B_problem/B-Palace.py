N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

close_av_temp = 0
temp_list = []

for i in range(N):
    close_av_temp = abs(A - (T - H[i] * 0.006))
    temp_list.append(close_av_temp)

print(temp_list.index(min(temp_list)) + 1)


# -------------
N = input()
T, A = map(int, input().split())

x = [abs(A - (T - 0.006 * H)) for H in list(map(int, input().split()))]

print(x.index(min(x)) + 1)


# -------------
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temp = [0] * N
for i in range(N):
    temp[i] = abs(A - (T - H[i] * 0.006))

print(temp.index(min(temp)) + 1)
