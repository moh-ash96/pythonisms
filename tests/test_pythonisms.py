from pythonisms import __version__
import pytest
from pythonisms.pythonisms import Linked_list,Node


def test_version():
    assert __version__ == '0.1.0'



def test_for_in(ll_test):
  result = 0
  for i in ll_test:
    result += 1
  assert result == 3

def test_list_comprehension(ll_test):
    li = []
    for node in ll_test:
        li.append(node)
    assert li == [10,20,30,40]

def test_convert_list_to_tuple(ll_test):
    assert tuple(ll_test) == (10,20,30,40)

# Can successfully check two Linked_lists are equal
def test_equal(ll_test , ll_test2):
  assert (ll_test == ll_test2)

def test_not_equal (ll_test,ll_test3):
  assert not (ll_test == ll_test3)

def test_truthy(ll_test):
    assert ll_test

def test_falsy():
    ll = Linked_list()
    assert not ll

@pytest.fixture
def ll_test():
  ll=Linked_list()
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


    
