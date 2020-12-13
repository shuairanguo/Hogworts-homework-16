import pytest




class Test_demo():

    def test_one(self,myfixture):
        print("执行testone")

    def test_two(self,myfixture):
        print("执行testtwo")

    def test_three(self):
        print("three")