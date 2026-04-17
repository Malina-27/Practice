student = {
    "name": "Ali",
    "age": 20,
    "city": "Almaty"
}

print(student)
# {'name': 'Ali', 'age': 20, 'city': 'Almaty'}




student = {
    "name": "Ali",
    "age": 20,
    "city": "Almaty"
}

print(student["age"])
# 20




student = {
    "name": "Ali",
    "age": 20
}

student["grade"] = "A"

print(student)
# {'name': 'Ali', 'age': 20, 'grade': 'A'}



student = {
    "name": "Ali",
    "age": 20,
    "city": "Almaty"
}

for key, value in student.items():
    print(key, value)
# name Ali
# age 20
# city Almaty



text = "apple banana apple orange banana apple"

words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
# {'apple': 3, 'banana': 2, 'orange': 1}



names = ["Ali", "Sara", "Omar"]
scores = [90, 85, 88]

result = dict(zip(names, scores))

print(result)
# {'Ali': 90, 'Sara': 85, 'Omar': 88}



scores = {
    "Ali": 90,
    "Sara": 85,
    "Omar": 95
}

best = max(scores, key=scores.get)

print(best)
# Omar