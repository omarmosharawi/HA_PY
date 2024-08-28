founder = {
    'name': 'Omar Mohamed Sharawi',
    'age': 21,
    'title': 'Software Engineer',
    'salary': 70000,
    'skills': ['Python', 'JavaScript', 'PHP']
}
print(founder['name'] + ' receive ' + str(founder['salary']) + '$ per year')

print('-'*30)
# get() function returns the value associated with the user-specified key.
print(founder['name'] + ' receive ' + str(founder.get('salary', 'not specified')) + '$ per year')   # will print not specified if not found the salary key

print('-'*30)
# setdefault() function returns the value of the specified key.
print(founder)
print(founder['name'])
print(founder.setdefault('name', 'Adel'))   # return new value of key if specified key not found
founder.setdefault('level', 3)
print(founder)  # will add new key with value
# another way to add but in many code lines
if 'skills' not in founder:
    founder['skills'] = 'Python'
print(founder)

print('-'*30)
# update() function is used to add and update dictionary items.
print(founder)
founder.update({'salary': 100000})
print(founder)
# can add new key with new value if not found the specific key
founder.update({'address': 'New Cairo'})
print(founder)

print('-'*30)
# clear() function is used to clear or remove all value.
print(founder)
founder.clear()
print(founder)