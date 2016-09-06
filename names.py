users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ]
 }
users1 = {
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
     ]
}
for key, data in users.items():
	print('students')
 	for value in data:
 		print value["first_name"], value["last_name"], (len(value["first_name"])+len(value["last_name"]))
for key, data in users1.items():
	print('instructors')
	for value in data:
		print value["first_name"], value["last_name"], (len(value["first_name"])+len(value["last_name"]))


