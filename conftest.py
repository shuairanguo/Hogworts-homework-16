import pytest

from pythoncode.calculator import Calculator


@pytest.fixture()
def myfixture():
    print("执行我的fixture")


@pytest.fixture(params=["参数1", "参数2"])
def login(request):
    print("开始登陆！")
    yield request.param
    print("执行teardown，关闭浏览器")


@pytest.fixture(scope="module")
def cal():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("计算结束")
