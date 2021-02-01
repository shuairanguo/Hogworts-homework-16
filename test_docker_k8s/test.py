from selenium import webdriver

# firefox_capabilities = {
#     "browserName": "chrome",
#     "version": "58.0",  # 注意版本号一定要写对
#     "platform": "ANY",
#     "javascriptEnabled": True,
#     "marionette": True,
# }

desired_capabilities={'browserName': 'chrome'}
browser = webdriver.Remote("http://192.168.1.102:4444/wd/hub",
                           desired_capabilities=desired_capabilities)  # 注意端口号4444是我们上文中映射的宿主机端口号
browser.get("http://www.baidu.com")
browser.get_screenshot_as_file(r"./baidu.png")


# from time import sleep
# from selenium import webdriver

#
# driver = webdriver.Remote(
# command_executor='http://192.168.1.102:4444/wd/hub',
# desired_capabilities={'browserName': 'chrome'}
# )
#
# driver.get('https://www.baidu.com')
# print("start run")
# sleep(1)
# print(driver.title)
# driver.quit()
# print("end...")
