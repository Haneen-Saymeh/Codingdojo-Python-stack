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

x[1][0]=15
print(x)

students[0]["last_name"]="Bryant"
print(students)

sports_directory["soccer"][0] = "Andree"
print(sports_directory)

z[0]["y"]=30
print(z)



def iterateDictionary(students):
    for i in students:
        for key in i.keys():
            print(key)
        for value in i.values():
            print(value)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
students = [
{'first_name':  'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print(iterateDictionary(students))


def iterateDictionary2(key_name, some_list):
    for k in some_list:
        print(k[key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(dojo):
    print(len(dojo['locations']), "LOCATIONS")
    for location in dojo['locations']:
        print(location)
    print()
    print(len(dojo['instructors']), "INSTRUCTORS")
    for instructor in dojo['instructors']:
       print(instructor)
       
printInfo(dojo)