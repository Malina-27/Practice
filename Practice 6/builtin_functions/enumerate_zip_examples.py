# 1. enumerate
for i, name in enumerate(["Ali", "Sara"]):
    print(i, name)
# Output:
# 0 Ali
# 1 Sara

# 2. enumerate start
for i, name in enumerate(["Ali", "Sara"], start=1):
    print(i, name)
# Output:
# 1 Ali
# 2 Sara

# 3. zip
for a, b in zip([1,2], ["a","b"]):
    print(a, b)
# Output:
# 1 a
# 2 b

# 4. sorted
print(sorted([3,1,2]))
# Output: [1, 2, 3]

# 5. базовые функции
print(len([1,2,3]))
print(min([1,2,3]))
print(max([1,2,3]))
print(sum([1,2,3]))
# Output:
# 3
# 1
# 3
# 6