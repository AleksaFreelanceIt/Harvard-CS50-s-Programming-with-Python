# User must input integers or else there will be an error
x = int(input("What is x? "))
y = int(input("What is y? "))

print(x+y)

# User must input numbers or else there will be an error
a = float(input("What is a? "))
b = float(input("What is b? "))

#Prints out rounded up to the nearest integer
print(round(a+b))
#Adds a comma when above a thousand
print(f"{(a+b):,}")

c = round(a/b, 2)
print(c)