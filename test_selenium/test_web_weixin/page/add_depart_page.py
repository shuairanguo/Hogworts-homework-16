import time

from selenium.webdriver.common.by import By

from test_selenium.test_web_weixin.page.base_page import BasePage
from test_selenium.test_web_weixin.page.contact_page import ContactPage


class AddDepart(BasePage):
    _location_add = (By.XPATH, '//a[text()="添加部门"]')
    _location_deprtname = (By.XPATH, '//input[@class="qui_inputText ww_inputText"]')
    _location_belong_depart = (By.XPATH, '//a[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]')
    _location_belong_depart_select = (By.XPATH, '//a[text()="软件"]')
    _location_confirme = (By.XPATH, "//a[text()='确定']")

    def add_depart(self):
        """添加部门操作
        :return:
        """

        self.driver.find_element(*self._location_add).click()
        self.driver.find_element(*self._location_deprtname).send_keys("开发一部")
        self.driver.find_element(*self._location_belong_depart).click()
        departs = self.driver.find_elements(*self._location_belong_depart_select)
        departs[-1].click()
        self.driver.find_element(*self._location_confirme).click()
        time.sleep(2)
        self.driver.refresh()
        return ContactPage(self.driver)
