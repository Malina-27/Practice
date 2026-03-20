import shutil, os

# 1. move
shutil.move("file.txt", "dir1/file.txt")
print("Moved")
# Output: Moved

# 2. copy
shutil.copy("dir1/file.txt", "copy.txt")
print("Copied")
# Output: Copied

# 3. move обратно
shutil.move("dir1/file.txt", "file.txt")
print("Moved back")
# Output: Moved back

# 4. list inside
print(os.listdir("dir1"))
# Output: []

# 5. удалить папку
os.rmdir("dir1")
print("Deleted dir")
# Output: Deleted dir