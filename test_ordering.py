import pytest

@pytest.mark.run(order=2)
def test_order2():
    print("执行 test order2")

@pytest.mark.run(order=1)
def test_order1():
    print("执行 test order1")