import pytest

from test_selenium.test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        # 第一次实例化
        self.main = MainPage()

    def test_add_depart(self):
        """添加部门测试用例
        :return:
        """
        #1.跳转添加成员页面  2. 添加成员 3. 自动跳转到通讯录页面
        res = self.main.goto_add_depart().add_depart().get_depart()
        print('res')
        print(res)
        assert "开发一部" in res



    # 回复到首页还原一开始的状态
    def teardown(self):
        self.main.back_main()

