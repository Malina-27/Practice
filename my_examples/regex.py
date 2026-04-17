'''import re
a=input()
if re.match(r"Hello", a):
    print("Yes")
else:
    print("No")'''

'''import re
s=input()
p=input()
if re.search(p, s):
    print("Yes")
else:
    print("No")'''


'''import re
a=input()
b=input()
c=re.findall(b, a)
print(len(c))'''

'''import re
a=input()
b=re.findall(r"\d", a)
print(" ".join(b))
'''
import re
a=input()
if re.match(r"^[A-Ba-b].*[0-9]$", a):
    print("Yes")
else:
    print("No")