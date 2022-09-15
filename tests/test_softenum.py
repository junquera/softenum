import pytest
from softenum import __version__
from softenum import Softenum

def test_version():
    assert __version__ == '0.1.0'


class A(str, Softenum):

    a = "a"
    

def test():
    
    assert A.a == A('a')
    assert A.a != A('A')
    assert A(A.a) == A.a


    try:
        class X(str, Softenum):
            enumerated = {"1": "jejeje"}
    except:
        assert True

    try:
        class X(str, Softenum):
            _enumerated = "jejeje"
    except:
        assert True


    class X(Softenum):
        enumerated = "jejeje"

    class X(int, Softenum):
        a = 1

    try:
        A.be
    except:
        assert True

    try:
        A(b"\xDE\xAD\xBE\xEF")
    except:
        assert True

    try:
        A("_x")
        A("*x")
        A("\x00")
    except:
        assert True


    print(A("cE"))
    print(A("Ce"))

    print(type(A.a))
    print(type(A('a')))

if __name__ == "__main__":
    test()
