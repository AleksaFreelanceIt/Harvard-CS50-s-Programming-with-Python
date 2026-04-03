#with open("people.csv") as file:
#    for line in sorted(file):
#        name, age = line.rstrip().split(",")
#        print(f"{name} is {age} years old.")


#people = []
#with open("people.csv") as file:
#    for line in file:
#        name, age = line.rstrip().lower().title().split(",")
#        people.append(f"{name} is {age} years old.")
#
#for person in sorted(people):
#    print(person)

#people = []
#with open("people.csv") as file:
#    for line in file:
#        name, age = line.rstrip().lower().title().split(",")
#        person = {}
#        person["name"] = name
#        person["age"] = age
#        people.append(person)
#
#for person in people:
#    print(f"{person['name']} is {person['age']} years old!")

#people = []
#with open("people.csv") as file:
#    for line in file:
#        name, age = line.rstrip().lower().title().split(",")
#        person = {"name": name, "age": age}
#        people.append(person)
#
#def get_name(person):
#    return person["name"]
#def get_age(person):
#    return person["age"]
#
#sorting by either name or gae using the key= 
#for person in sorted(people, key=get_name):
#    print(f"{person['name']} is {person['age']} years old!")
#
#using anon function for sorting
#for person in sorted(people, key=lambda person: person["name"]):
#   print(f"{person['name']} is {person['age']} years old!")

import csv
people = []
with open("people.csv") as file:
    #reader handles edge cases in csv files
    #reader = csv.reader(file)
    reader = csv.DictReader(file)
    #for name, age in reader:
    #    people.append({"name": name, "age": age})
    for row in reader:
        people.append({"name": row["name"].lower().title(),"age":row["age"]})

for person in sorted(people, key=lambda person: person["name"]):
   print(f"{person['name']} is {person['age']} years old!")