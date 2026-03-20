# sample.txt:
# Hello
# World

import os

# 1. read()
with open("sample.txt", "r") as f:
    print(f.read())
# Output:
# Hello
# World

# 2. readline()
with open("sample.txt", "r") as f:
    print(f.readline())
# Output:
# Hello

# 3. readlines()
with open("sample.txt", "r") as f:
    print(f.readlines())
# Output:
# ['Hello\n', 'World']

# 4. чтение через цикл
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
# Output:
# Hello
# World

# 5. проверка существования
print(os.path.exists("sample.txt"))
# Output:
# True