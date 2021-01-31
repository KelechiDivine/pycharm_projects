from testing_In_Python import *


def run_tests():
    assert add(2, 3) == 5
    assert subtract(3, 2) == 1
    assert division(4, 2) == 2
    assert square(2) == 4
    assert square_root(64) == 8


if __name__ == '__main__':
    run_tests()
