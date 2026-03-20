import os

# 1. текущая директория
print(os.getcwd())
# Output: (путь к папке)

# 2. mkdir
os.mkdir("dir1")
print("Directory created")
# Output: Directory created

# 3. makedirs
os.makedirs("a/b/c")
print("Nested dirs created")
# Output: Nested dirs created

# 4. listdir
print(os.listdir())
# Output: ['dir1', 'a', 'file.txt']

# 5. chdir
os.chdir("dir1")
print(os.getcwd())
# Output: .../dir1