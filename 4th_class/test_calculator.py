from calculator import square
def main():
    test_square()
# Unit testing usually means testing individual units/functions of code
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2*2 was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3*3 was not 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3*-3 was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0*0 was not 0")
    

if __name__ == "__main__":
    main()