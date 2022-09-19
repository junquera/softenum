import pytest
from softenum import __version__
from softenum import Softenum

def test_version():
    assert __version__ == '0.1.0'    

def test_str():

    class A(str, Softenum):
        a = "a"
    
    assert A.a == A('a')
    assert A.a != A('A')
    assert A(A.a) == A.a

    assert (A("cE"))
    assert (A("Ce"))

def test_novalue():

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

def test_no_super():

    class X(Softenum):

        enumerated = "jejeje"

def test_int():

    class A(int, Softenum):

        a = 1
    
    assert A.a == A(1)
    assert A(A.a) == A.a

def test_noval():

    class A(Softenum):
        pass

    try:
        A.be
    except:
        assert True

def test_badclass():

    class A(int, Softenum):

        a = 1

    try:
        A(b"\xDE\xAD\xBE\xEF")
    except:
        assert True


def test_fuzz():

    class A(str, Softenum):
        a = "oneval"

    try:
        A("_x")
        A("*x")
        A("\x00")
    except:
        assert True

