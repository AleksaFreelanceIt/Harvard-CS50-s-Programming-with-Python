def main()
    print_square(3)

def print_square(n):
    #for each row in square
    for i in range(n):
        #for each brick in row
        for j in range(n):
            #print brick
            print("#",end="")
        print()
def print_square2(n):
    for i in range(n):
        print("#" * n)

main()