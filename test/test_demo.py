import pytest
@pytest.fixture
def before_test():
    print('Before test')
    yield
    print('\nAfter test')

def test_demo1():
    assert 1==1

def test_demo2(before_test):
    assert 2==2


