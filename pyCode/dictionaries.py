task = {
    'id': 1,
    'name': 'study network',
    'done': True
}
print('1)', type(task), end=' ') # dictionary
print('2)', task)

# another way to create a dictionary
task2 = dict([('id',2), ('name','study database'), ('done', False)])
print('3)', type(task2), end=' ')
print('4)', task2)

# another way to create a dictionary
task3 = dict(id= 3, name= 'study programming', done= False)
print('5)', type(task3), end=' ')
print('6)', task3)

# print(task[0]) # this an error because in dictionary using key not an index or a position
print('7)', task['id'])

employees = {2: 'Mohamed', 1: 'Omar', 3:'Ahmed'}
print('8)', employees[1]) # we can use the value of the key as a key for other dictionaries if keys are integer

task2['done'] = True # we can modify the dictionary by adding new data
task2['date'] = 'today' # we can add new value
print('8)', task2)



# another way to create a dictionary
newTask = {}

newTask['id'] = 7
newTask['name'] = 'create a website'
newTask['priority'] = ['none', 'low', 'medium', 'large']
newTask['notes'] = {1: 'html', 2: 'css', 3: 'js', 4:'php', 5:'sql'}
newTask['due'] = ('yesterday', 'today', 'tomorrow')
newTask['isDone'] = True
print('9)', type(newTask), end=' ')
print('10)', newTask)

taskPriority = newTask['priority'][3]
taskDuration = newTask['due'][2]

print('11)', f'Task priority is {taskPriority} and it will be finished within {taskDuration}.')

# can't add a new item with the same name as existing one so it will replace the old one.
newTask['name'] = 'create a big website using express framework'
print('12)', newTask)



# can use del as example del newTask['name'] to remove the whole entry from the dictionary
# can use len as example len(newTask) to get how many items are there in the dictionary
# can use clear() method as example newTask.clear() to delete all entries in the dictionary
# can use get() method as example result = newTask.get('name','no such name') if 'name' in newTask else 'no such name'
# can use popitem() method as example next(newTask.popitem()) to return and remove a (key ,value) pair from the dictionary
# can use pop() method as example result = newTask.pop('id') to remove the id entry and return its value

#  you can access all keys of the dictionary  using items() method
for id, name in newTask.items():
    print('13)', f"{id}: {name}")

# you can use values() method to get only the values from the dictionary
for taskDuration in newTask.values():
    if taskDuration == 'tomorrow': print('14)', 'The deadline date is tomorrow')
    # else: print('please hurry up to finish it today')

# you can also use keys() method to get only the keys from the dictionary
for key in newTask.keys():
    print('15)', key)



# can get list from dictionary
print('16)', list(newTask))
print('17)', list(newTask['priority']))
print('18)', list(key))
