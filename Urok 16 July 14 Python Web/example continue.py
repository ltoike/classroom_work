import json


with open("example.txt", encoding="utf-8") as myfile:
    request = json.load(myfile)

request['city'] = 'Almaty'

open ("example.txt", "w", encoding="utf-8") as myfile:
    json.dump(request, myfile, ensure_ascii=False)