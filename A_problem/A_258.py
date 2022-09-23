K = int(input())
apple = "2" + str(1 + K // 60)
if 0 <= K <= 9 or 60 <= K <= 69:
    orange = "0" + str(K % 60)
else:
    orange = str(K % 60)

print(apple + ":" + orange)
