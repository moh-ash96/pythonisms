from pythonisms import __version__
import pytest
from pythonisms.pythonisms import (
    Linked_list,
    Node,
    validate_conditions,
    calculate_time,
    slowdown,
    debug_code,
    convert_to_float,
)


def test_version():
    assert __version__ == "0.1.0"


def test_for_in(ll_test):
    result = 0
    for i in ll_test:
        result += 1
    assert result == 4


def test_list_comprehension(ll_test):
    li = []
    for node in ll_test:
        li.append(node)
    assert li == [10, 20, 30, 40]


def test_convert_list_to_tuple(ll_test):
    assert tuple(ll_test) == (10, 20, 30, 40)


# Can successfully check two Linked_lists are equal
def test_equal(ll_test, ll_test2):
    assert ll_test == ll_test2


def test_not_equal(ll_test, ll_test3):
    assert not (ll_test == ll_test3)


def test_truthy(ll_test):
    assert ll_test


def test_falsy():
    ll = Linked_list()
    assert not ll

def test_calculate_time(capsys):
    @calculate_time
    def check_equality(a, b):
        return a == b
    
    check_equality(5,5)
    result = capsys.readouterr()
    assert float(result.out) > 0

def test_slow_down(capsys):
    
    @calculate_time
    def check_equality(a, b):
        return a == b
    check_equality(5,5)
    result1 = capsys.readouterr()

    @calculate_time
    @slowdown
    def check_equality_slow(a, b):
        return a == b
    check_equality_slow(5,5)
    result2 = capsys.readouterr()

    assert float(result2.out) > float(result1.out)
    
def test_debug_code(capsys):
    @debug_code
    def add(a, b):
        return a + b
    
    add(3,4)
    result = capsys.readouterr()

    assert result.out == "inputs are : (3, 4), {}\noutput is : 7\n"

def test_validate_true():
    @validate_conditions
    def calc_age(name, YOB):
        return f'Hello {name} you are {2021 - YOB} years old'
    
    assert calc_age('Dario', 1985) == 'Hello Dario you are 36 years old'

def test_validation_false():
    @validate_conditions
    def calc_age(name, YOB):
        return f'Hello {name} you are {2021 - YOB} years old'
    
    assert calc_age('Dario', '1985') == "passed arguments don't match"

def test_convert_return():
    @convert_to_float
    def add(a, b):
        return a + b
    assert add(3, 4) == 7.0


@pytest.fixture
def ll_test():
    ll = Linked_list()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    return ll


@pytest.fixture
def ll_test2():
    ll = Linked_list()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    return ll


@pytest.fixture
def ll_test3():
    ll = Linked_list()
    ll.append(100)
    ll.append(200)
    return ll
