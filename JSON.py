import json

data = {
    'firstnamen' : 'Lando',
    'lastname' : 'Norris',
    'age' : '25',
    'hobbies' : [
        'Racing',
        'Playing'
    ]
}

data_json = json.dumps(data, indent=3)
print(data_json)

data = {
    'firstnamen' : 'George',
    'lastname' : 'Russell',
    'age' : '27',
    'hobbies' : [
        'Racing',
        'Farming'
    ]
}

file = open("data,json", "w")
json.dump(data, file)

data = {
    'firstnamen' : 'Fathimah',
    'lastname' : 'Karsan',
    'age' : '18',
    'hobbies' : [
        'Movies',
        'Gaming'
    ]
}

data_python = json.loads(data_json)
print( type(data_python))