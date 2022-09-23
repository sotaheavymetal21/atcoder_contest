str1 = input()
str2 = str1.replace("eraser", "")
print(str2)
str2 = str2.replace("erase", "")
print(str2)
str2 = str2.replace("dreamer", "")
print(str2)
str2 = str2.replace("dream", "")
print(str2)
if str2 == "":
    print("YES")
else:
    print("NO")


S = input()
Sd1 = S.replace("eraser", "").replace("erase", "").replace(
    "dreamer", "").replace("dream", "")
if Sd1 == "":
    print("YES")
else:
    print("NO")
