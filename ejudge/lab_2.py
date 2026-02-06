# 201
a=int(input())
if (a%4==0 and a%100!=0) or a%400==0:
  print("YES")
else:
  print("NO")


# 202
n=int(input())
s=0
for i in range(1,n+1):
  s+=i
print(s)


# 203
n = int(input())
a = list(map(int, input().split()))
sum = 0
for x in a:
    sum += x
print(sum)


# 204
n = int(input())
a = list(map(int, input().split()))
count = 0
for x in a:
    if x > 0:
        count += 1
print(count)


# 205
n = int(input())
p = 1
while p < n:
    p*= 2
if p == n:
    print("YES")
else:
    print("NO")


# 206
n = int(input())
a = list(map(int, input().split()))
maxv = a[0] 
for x in a:
    if x > maxv:
        maxv = x
print(maxv)


# 207
n = int(input())
a = list(map(int, input().split()))
maxv = a[0]
position = 1  
for i in range(n):
    if a[i] > maxv:
        maxv= a[i]
        position = i + 1
print(position)


# 208
n = int(input())
power = 1
while power <= n:
    print(power, end=' ')
    power *= 2


# 209
n = int(input())
a = list(map(int, input().split()))
maxv = a[0]
minv = a[0]
for x in a:
    if x > maxv:
        maxv = x
    if x < minv:
        minv = x
for i in range(n):
    if a[i] == maxv:
        a[i] = minv
print(*a)


# 210
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)  
print(*a)


# 211
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
l -= 1
r -= 1
while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1
print(*a)


# 212
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] ** 2
print(*a)


# 213
n = int(input())
s=0
if n < 2:
    print("No")
else:
    for i in range(2, n + 1):
        if n % i == 0:
            s+=1
    if s==1:
        print("Yes")
    else:
        print("No")


# 214
n = int(input())
a = list(map(int, input().split()))
frequency = {} 
for x in a:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1
max_freq = max(frequency.values())
most_frequent = min(key for key, val in frequency.items() if val == max_freq)
print(most_frequent)


# 215
n = int(input())
surnames = set()
for _ in range(n):
    surname = input().strip()
    surnames.add(surname)
print(len(surnames))


# 216
n = int(input())
a = list(map(int, input().split()))
seen = set()
for x in a:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)


# 217
n = int(input())
numbers = {}
for _ in range(n):
    num = input().strip()
    if num in numbers:
        numbers[num] += 1
    else:
        numbers[num] = 1
count = 0
for val in numbers.values():
    if val == 3:
        count += 1

print(count)


# 218
n = int(input())
strings = []

for _ in range(n):
    s = input().strip()
    strings.append(s)

first_index = {}

for i, s in enumerate(strings):
    if s not in first_index:
        first_index[s] = i + 1
for s in sorted(first_index):
    print(s, first_index[s])


#219
n = int(input())
episodes = {}

for _ in range(n):
    line = input().split()
    dorama = line[0]
    k = int(line[1])
    
    if dorama in episodes:
        episodes[dorama] += k
    else:
        episodes[dorama] = k
for dorama in sorted(episodes):
    print(dorama, episodes[dorama])


# 220
n = int(input())
document = {}

for _ in range(n):
    command = input().split()
    if command[0] == "set":
        key = command[1]
        value = command[2]
        document[key] = value 
    elif command[0] == "get":
        key = command[1]
        if key in document:
            print(document[key])
        else:
            print(f"KE: no key {key} found in the document")


