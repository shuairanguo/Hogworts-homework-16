from test_appium.po.page.address_list_page import AddressListPage


class MainPage:

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        return AddressListPage()
