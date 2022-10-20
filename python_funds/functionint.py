x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15

x[1][0] =15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]["last_name"]="Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0]="Andres"
print(sports_directory)

# Change the value 20 in z to 30
z[0]["y"]=30
print(z)

# Iterate Through a List of Dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for dicts in list:
        for key, value in dicts.items():
            print(key,value)

print(iterateDictionary(students))



# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dicts in some_list:
        print(dicts[key_name])
print(iterateDictionary2("last_name",students))


# Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for i in some_dict[key]:
            print(i)
        

print(printInfo(dojo))


    



