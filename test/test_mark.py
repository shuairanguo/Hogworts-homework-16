import pytest

class Test_demo():

    @pytest.mark.demo
    def test_demo(self):
        print("first")

    @pytest.mark.smoke
    def test_second(self):
        print("second")