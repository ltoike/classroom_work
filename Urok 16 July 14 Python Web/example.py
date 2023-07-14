import json


data = '{"type": "forecast", "duration": 3, "city": "Karaganda", "country_code": "kz"}'

request = json.loads(data) #в словарь

request['city'] = "Almaty" #из словаря в строку

data = json.dumps(request, ensure_ascii=False)
print(data)
