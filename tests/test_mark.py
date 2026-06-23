import pytest

@pytest.mark.smoke
def test_login():
    print("This is login test smoke test")
    assert True

@pytest.mark.regression
def test_cart():
    print("This is regression test cart test")
    assert True

# @pytest.mark.skip
# def test_skipped():
#     print("This is skipped test")
#
# @pytest.mark.skipif(True, reason="Not Ready")
# def test_ready():
#     pass
#
# @pytest.mark.xfail
# def test_demo():
#     assert False