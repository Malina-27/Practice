import shutil, os

# 1. copy
shutil.copy("file.txt", "copy.txt")
print("Copied")
# Output: Copied

# 2. copy2
shutil.copy2("file.txt", "copy2.txt")
print("Copied with metadata")
# Output: Copied with metadata

# 3. move
shutil.move("copy.txt", "moved.txt")
print("Moved")
# Output: Moved

# 4. delete
os.remove("moved.txt")
print("Deleted")
# Output: Deleted

# 5. обработка ошибки
try:
    os.remove("no.txt")
except FileNotFoundError:
    print("File not found")
# Output: File not found