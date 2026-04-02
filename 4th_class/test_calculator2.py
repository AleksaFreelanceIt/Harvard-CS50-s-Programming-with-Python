from calculator import square

def test_pos_square():
    assert square(2) == 4
    assert square(3) == 9
def test_neg_square():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero_square():
    assert square(0) == 0