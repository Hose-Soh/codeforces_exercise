import re

lucky_numbers = [
    4, 7,
    44, 47, 74, 77,
    444, 447, 474, 477, 744, 747, 774, 777
]

n = input()

pattern = r"[0-3,5-6,8-9].*"

find = re.search(pattern, n)

flag = False
for i in lucky_numbers:
    if int(n)%i==0:
        flag = True
        break


if not find:
    print("YES")

elif flag:
    print("YES")
else:
    print("NO")
