import logging
from appium import webdriver

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_frame.black_handler import black_wrapper


class BasePage:
    FIND = 'find'
    ACTION = 'action'
    FIND_AND_CLICK = 'find_and_click'
    SEND = 'send'
    CONTENT = 'content'

    def __init__(self, driver: WebDriver = None):
        # 定义了一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["#deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.adnriod"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # noReset 保留缓存， 比如登录状态
        caps["noReset"] = "True"
        # 不停止应用，直接运行测试用例
        # caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = 'true'
        caps['skipServerInstallation'] = 'true'
        # caps["settings[waitForIdleTimeout]"] = 0
        # 关键  localhost:4723  本机ip:server端口
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')
    def send(self,by,locator,content):
        self.find(by,locator).send_keys(content)

    def find_by_swip(self, driver, by, locator):
        self.driver.implicitly_wait(1)
        elements = self.driver.find_elements(by, locator)
        while len(elements) == 0:
            self.driver.swipe(0, 0, 0, 20)
            elements = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)

    @staticmethod
    def find_by_swip2(driver: WebDriver, by, locator) -> WebElement:
        driver.implicitly_wait(1)
        elements = driver.find_elements(by, locator)
        while len(elements) == 0:
            driver.swipe(0, 600, 0, 400)
            elements = driver.find_elements(by, locator)
        driver.implicitly_wait(5)
        return elements[0]

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

    def load(self,yaml_path):
        with open(yaml_path,encoding='utf-8') as f:
            data = yaml.load(yaml_path)
        fro step in data:
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            if action == self.FIND_AND_CLICK:
                self.find(By.XPATH,xpath_expr)
            elif action == self.SEND:
                content = step.get(self.CONTENT)
                self.send(By.XPATH,xpath_expr,content)

    def screenshot(self,picture_path):
        self.driver.save_screenshot(picture_path)
