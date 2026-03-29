#def is the keyword used to define functions, in Python indentation matters
def main():
    name = input("What's your name? ").strip().title()
    hello(name)

#to = "World" sets the default value of variable to to World
def hello(to="World"):
    print("Hello", to)

main()