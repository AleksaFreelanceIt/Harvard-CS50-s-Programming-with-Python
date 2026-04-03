#with open("names.txt","r") as file:
#    lines =  file.readlines()
#
#for line in lines:
#    #to remove the \n symbol from each line of the file we can use .rstrip()
#    print("hello,", line.rstrip())


#with open("names.txt","r") as file:
#    for line in file:
#        print("hello,", line.rstrip().lower().title())


#names = []
#with open("names.txt") as file:
#    for line in file:
#        names.append(line.rstrip().lower().title())
#
#for name in sorted(names):
#    print(f"hello, {name}")


with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip().lower().title())