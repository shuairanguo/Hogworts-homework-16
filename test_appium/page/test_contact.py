from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup(self):
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
        self.driver.implicitly_wait(15)

    def test_contact(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录'] and @resource-id = 'com.tencent.wework:id/elq'")

        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contians(@text,'姓名')]/..//*[@text='必填']").send_keys('aaaaa')
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"性别")]/..//*[@text="男"]').click()

        def wait_ele_for(driver:WebDriverWait):
            eles = driver.find_elements(MobileBy.XPATH,'//*[@text="女"]')
            return len(els)
        WebDriverWait(self.driver,10).until(wait_ele_for)

        self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手机]/..//*[@text="手机号"]').send_keys('13322223333')
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()




