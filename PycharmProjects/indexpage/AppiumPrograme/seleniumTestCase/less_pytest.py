import pytest
def reverse(string):
    return string[len(string)::-1]

def test_reverse():

    string = "KCUF"
    assert reverse(string) == "FUCK"


test_reverse()

