from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.contactadd_page import ContactAddPage


class MemberInviteMenuPage(BasePage):

    def add_member_menual(self):
        # 点击【手动输入添加】
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.get_toast_text()
        return result
