#file = open("names.txt", "a")
#for _ in range(3):
#    name = input("What's your name? ")
#    file.write(name+"\n")
#file.close()

name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")