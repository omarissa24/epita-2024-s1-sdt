import json

JSON_FILE_PATH = 'resources/json/users.json'

class User:
    def __init__(self, id, name, city, school, age, is_teacher):
        self.id = id
        self.name = name
        self.city = city
        self.school = school
        self.age = age
        self.is_teacher = is_teacher

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, City: {self.city}, School: {self.school}, Age: {self.age}, Is teacher: {self.is_teacher}"
    
    def __repr__(self):
        return f"ID: {self.id}, Name: {self.name}, City: {self.city}, School: {self.school}, Age: {self.age}, Is teacher: {self.is_teacher}"
    

def parse_row(row):
    id = row['id']
    name = row['name']
    city = row['city']
    school = row['school']
    age = row['age']
    is_teacher = row['is_teacher']
    return User(id, name, city, school, age, is_teacher)

with open(JSON_FILE_PATH) as jsonfile:
    users = json.load(jsonfile)
    users = [parse_row(row) for row in users]
    for user in users:
        print(user)
        print()
        