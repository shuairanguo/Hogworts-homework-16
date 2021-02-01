from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.member_invite_menu_page import MemberInviteMemberPage


class AddressListPage(BasePage):

    def click_addmember(self):
        """
        添加成员
        :return:
        """
        # todo
        self.find_click(MobileBy.XPATH,'')
        return MemberInviteMemberPage()