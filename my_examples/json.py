import json
data = '{"name": "Ali", "age": 20}'
result = json.loads(data)
print(result)
# loads() превращает JSON → Python dictionary


import json
student = {
    "name": "Ali",
    "age": 20
}
result = json.dumps(student)
print(result)
# dumps() превращает Python dictionary → JSON 
'''
| Python   | JSON     |
| -------- | -------- |
| `'text'` | `"text"` |
| `True`   | `true`   |
| `None`   | `null`   | '''


# Чтение JSON файла
'''Файл data.json
{
  "name": "Omar",
  "age": 19,
  "city": "Shymkent"
} '''
import json
with open("data.json") as f:
    data = json.load(f)
print(data["city"])


# Запись JSON в файл
import json
data = {
    "name": "Ali",
    "age": 20
}
with open("data.json", "w") as f:
    json.dump(data, f)

'''Это создаст файл data.json
{"name": "Ali", "age": 20}'''



#💡 Самые важные функции JSON
'''функция	    что делает
json.loads()	JSON → Python
json.dumps()	Python → JSON
json.load()	   JSON файл → Python
json.dump()	   Python → JSON файл'''