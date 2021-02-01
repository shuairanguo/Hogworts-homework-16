from appium import webdriver

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps = {}
            desired_caps["platformName"] = "Android"
            # desired_caps["deviceName"] = "emulator-5554"
            desired_caps["deviceName"] = "dcd7fa16"
            # desired_caps["platformVersion"] = "6.0.1"
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
            desired_caps["noReset"] = "true"
            desired_caps['skipServerInstallation'] = "true"
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            # 设置页面等待空闲状态的时间
            desired_caps['setting[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(15)

    def goto_main(self):
        return MainPage()
