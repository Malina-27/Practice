# 301
n = input()

is_valid = True

for digit in n:
    if int(digit) % 2 != 0:
        is_valid = False
        break

if is_valid:
    print("Valid")
else:
    print("Not valid")





# 302
def isUsual(num):
    if num <= 0:
        return False

    for divisor in [2, 3, 5]:
        while num % divisor == 0:
            num //= divisor

    return num == 1


n = int(input())

if isUsual(n):
    print("Yes")
else:
    print("No")





# 303
def decode_number(s):
    codes = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3",
        "FOU": "4", "FIV": "5", "SIX": "6",
        "SEV": "7", "EIG": "8", "NIN": "9"
    }

    number = ""
    for i in range(0, len(s), 3):
        number += codes[s[i:i+3]]

    return int(number)


def encode_number(num):
    codes = {
        0: "ZER", 1: "ONE", 2: "TWO", 3: "THR",
        4: "FOU", 5: "FIV", 6: "SIX",
        7: "SEV", 8: "EIG", 9: "NIN"
    }

    # если результат отрицательный
    if num < 0:
        return "MIN" + encode_number(-num)

    if num == 0:
        return "ZER"

    result = ""
    for digit in str(num):
        result += codes[int(digit)]

    return result


expression = input()

# ищем оператор
for op in "+-*":
    if op in expression:
        operator = op
        break

left, right = expression.split(operator)

num1 = decode_number(left)
num2 = decode_number(right)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    result = num1 * num2

print(encode_number(result))





# 304
class StringHandler:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input()

    def printString(self):
        print(self.text.upper())


obj = StringHandler()
obj.getString()
obj.printString()




# 305
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


n = int(input())
square = Square(n)
print(square.area())




#306
# Base class
class Shape:
    def area(self):
        return 0

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Read input
length, width = map(int, input().split())

# Create Rectangle object
rect = Rectangle(length, width)

# Print area
print(rect.area())





# 307
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# Ввод данных
x1, y1 = map(int, input().split())  # начальные координаты
x2, y2 = map(int, input().split())  # новые координаты для move
x3, y3 = map(int, input().split())  # координаты второй точки

# Создаем первый объект Point
p1 = Point(x1, y1)
p1.show()  # показываем начальные координаты

# Перемещаем точку
p1.move(x2, y2)
p1.show()  # показываем новые координаты

# Создаем второй объект Point
p2 = Point(x3, y3)

# Считаем расстояние и выводим
distance = p1.dist(p2)
print(f"{distance:.2f}")




# 308
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance

# Ввод данных
balance, withdraw_amount = map(int, input().split())

# Создаем аккаунт (можем дать любое имя владельца)
acc = Account("Owner", balance)

# Пытаемся снять деньги и выводим результат
print(acc.withdraw(withdraw_amount))




# 309
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Ввод радиуса
r = int(input())

# Создаем объект Circle
c = Circle(r)

# Выводим площадь с двумя знаками после запятой
print(f"{c.area():.2f}")




# 310
# Родительский класс
class Person:
    def __init__(self, name):
        self.name = name

# Дочерний класс
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)  # вызываем конструктор родителя
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

# Ввод данных
data = input().split()
name = data[0]
gpa = float(data[1])

# Создаем объект Student и выводим информацию
student = Student(name, gpa)
student.display()



# 311
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, other):
        return Pair(self.a + other.a, self.b + other.b)

# Ввод данных
a1, b1, a2, b2 = map(int, input().split())

# Создаем два объекта Pair
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

# Складываем пары
result = p1.add(p2)

# Выводим результат
print(f"Result: {result.a} {result.b}")





# 312
# Базовый класс Employee
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary

# Класс Manager
class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

# Класс Developer
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + 500 * self.completed_projects

# Класс Intern
class Intern(Employee):
    pass  # Наследует total_salary от Employee без изменений

# Чтение входных данных
data = input().split()
role = data[0]
name = data[1]
base_salary = int(data[2])

# Создаем соответствующий объект
if role == "Manager":
    bonus_percent = int(data[3])
    emp = Manager(name, base_salary, bonus_percent)
elif role == "Developer":
    completed_projects = int(data[3])
    emp = Developer(name, base_salary, completed_projects)
elif role == "Intern":
    emp = Intern(name, base_salary)
else:
    emp = Employee(name, base_salary)  # на случай другой роли

# Вывод результата
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")





# 313
import math

# Функция для проверки, простое ли число
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Чтение входных данных
nums = list(map(int, input().split()))

# Используем filter с lambda для отбора простых чисел
primes = list(filter(lambda x: is_prime(x), nums))

# Вывод результата
if primes:
    print(*primes)
else:
    print("No primes")




# 314
# Чтение данных
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# Применяем каждую операцию последовательно
for _ in range(q):
    op = input().split()
    
    if op[0] == "add":
        x = int(op[1])
        arr = list(map(lambda a: a + x, arr))
    elif op[0] == "multiply":
        x = int(op[1])
        arr = list(map(lambda a: a * x, arr))
    elif op[0] == "power":
        x = int(op[1])
        arr = list(map(lambda a: a ** x, arr))
    elif op[0] == "abs":
        arr = list(map(lambda a: abs(a), arr))

# Вывод результата
print(*arr)
