from functools import reduce

nums = [1, 2, 3, 4]

# 1. map
print(list(map(lambda x: x*2, nums)))
# Output: [2, 4, 6, 8]

# 2. map строки
print(list(map(str.upper, ["a", "b"])))
# Output: ['A', 'B']

# 3. filter
print(list(filter(lambda x: x % 2 == 0, nums)))
# Output: [2, 4]

# 4. filter строки
print(list(filter(lambda x: len(x) > 2, ["hi", "hello"])))
# Output: ['hello']

# 5. reduce
print(reduce(lambda x, y: x+y, nums))
# Output: 10