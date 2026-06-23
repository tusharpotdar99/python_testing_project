import pytest
pytestmark = pytest.mark.skip(reason="Skipping this test file")

@pytest.fixture(scope="function")
def browser():
    print("Opening Browser")
    yield
    print("Closing Browser")


@pytest.mark.parametrize("a,b,expected", [
    (2,3,5),
    (8,2,10),
    (10,30,40)
])

def test_addition(a,b,expected):
    assert a + b == expected


def test_login(browser):
    print("Login Test")


def test_relation():
    assert 10 >5

def test_string():
    assert "Hello" == "Hello"

def test_true():
    assert True

