def meow(n: int) -> None:   #type hint
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number) #using mypy to see type hints and var errors
meows: str = meow(number) #mypy will notice mismatch in types