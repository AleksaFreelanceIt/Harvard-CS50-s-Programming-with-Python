class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    #Getter
    @property
    def house(self):
        return self._house
    
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name.")
        self._name = name

def main():
    #name = get_name()
    #house = get_house()

    #student = get_student() #tuples are immutable
    #print(f"{student[0]} from {student[1]}")

    #student  = get_student()
    #if student["name"] == "Padma":
    #    student["house"] = "Ravenclaw"
    #print(f"{student['name']} from {student['house']} ")

    student = get_student()
    print (student)


#def get_name():
#    return input("Name: ")
#
#def get_house():
#    return input("House: ")

#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return name, house          #tuple

#def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    return {"name" : name, "house" : house}        #dictionary

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except ValueError:
        print("Invalid")
        return None
    
if __name__ == "__main__":
    main()