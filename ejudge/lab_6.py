# 601
n = int(input())
a = list(map(int, input().split()))
b = map(lambda x: x**2, a)
print(sum(b))

# 602
n = int(input())
a = list(map(int, input().split()))
b = filter(lambda x: x%2==0, a)
print(len(list(b)))

# 603
n = int(input())
a = input().split()
for i, v in enumerate(a):
    print(f"{i}:{v}", end=" ")

# 604
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for x, y in zip(a, b):
    s += x * y
print(s)

# 605
a = input()
c= "aeiouAEIOU"
if any(b in c for b in a):
  print("Yes")
else:
  print("No")

# 606
n=int(input())
a=list(map(int, input().split()))
if all(x>=0 for x in a):
  print("Yes")
else:
  print("No")

# 607
n = int(input())
a = input().split()
print(max(a, key=len))

# 608
n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))
print(*b)

# 609
n = int(input())
keys = input().split()
values = input().split()
query = input()
d = dict(zip(keys, values))
print(d.get(query, "Not found"))

# 610
n = int(input())
a = list(map(int, input().split()))
c = sum(map(bool, a))
print(c)