import json

json_data = '''{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing"],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}'''

slovar = {'name': 'Иван',
          'age': 30,
          'is_student': False,
          'courses': ['Python', 'QA Automation', 'API Testing'],
          'address': {
              'city': 'Москва',
              'zip': '101000'}
          }

pars = json.loads(json_data)             # из json в словарь
pars_2 = json.dumps(slovar, indent=2)    # из словаря в json


with open('js.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


with open('njs.json', 'w', encoding='utf-8') as file:
    json.dump(slovar, file, indent=2, ensure_ascii=False)

