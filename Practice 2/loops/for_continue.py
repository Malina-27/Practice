for i in range(5):
    if i == 2:
        continue
    print(i)
# 0 1 3 4


for x in range(6):
    if x % 2 == 0:
        continue
    print(x)
# 1 3 5


for c in "hello":
    if c == "l":
        continue
    print(c)
# h e o