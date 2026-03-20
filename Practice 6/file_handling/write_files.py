# 1. write()
with open("file.txt", "w") as f:
    f.write("Hello\n")
print("Done")
# Output: Done

# 2. несколько строк
with open("file.txt", "w") as f:
    f.write("A\nB\n")
print("Written")
# Output: Written

# 3. append
with open("file.txt", "a") as f:
    f.write("C\n")

with open("file.txt", "r") as f:
    print(f.read())
# Output:
# A
# B
# C

# 4. writelines()
lines = ["X\n", "Y\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)

with open("file.txt", "r") as f:
    print(f.read())
# Output:
# X
# Y

# 5. режим x
with open("new.txt", "x") as f:
    f.write("Created")
print("File created")
# Output: File created