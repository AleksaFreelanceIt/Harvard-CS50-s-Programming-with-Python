def main():
    n = int(input("What's n?"))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "sheep "*i #yield returns iterations of the loop, making it so that the program doesnt freeze if the input is too high

if __name__ == "__main__":
    main()