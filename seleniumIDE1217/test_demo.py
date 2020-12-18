import pytest
from selenium import webdriver

# chrome --remote-debugging-port=9222

class TestWework:

    def test_demo(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://www.baidu.com")
