import pytest
import yaml

from pythoncode.calculator import Calculator


class TestCalc:
    # def setup_class(self):
    #     self.calc = Calculator()
    #     print("开始计算")
    #
    # def teardown_class(self):
    #     print("结束计算")

    def get_datas():
        with open("../data.yml") as f:
            datas = yaml.safe_load(f)
            add_datas = datas["add"]
            sub_datas = datas["sub"]
            mul_datas = datas["mul"]
            div_datas = datas["div"]
            print(datas)
            return [add_datas,sub_datas, mul_datas,div_datas]

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    def test_add(self,cal, a, b, expect):
        assert expect == cal.add(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[1])
    def test_sub(self, cal,a, b, expect):
        assert expect == cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[2])
    def test_mul(self, cal,a, b, expect):
        assert expect == cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[3])
    def test_div(self, cal,a, b, expect):
        assert expect == cal.div(a, b)

