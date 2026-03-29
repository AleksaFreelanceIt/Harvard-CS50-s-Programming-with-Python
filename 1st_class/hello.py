# Hello World!
print("Hello World!")

# Puting the input into a variable
# You can also put the strip and title at the end of input
name = input("Hello, what is your name? ")

# .strip removes the whitespaces from strings. .title capitalizes the string
name = name.strip().title()

#Split's the users string by the space into the first and last names
first, last = name.split(" ")

print("Hello " + first)
# different time is to give arguments like print(arg1, arg2, arg3,...)

# you can change sep for what separates the arguments and end with what each print function ends
print("Hello", "Hello", sep=" ' ")
print("Hello", end="...")
