import time

import pytest
from selenium import webdriver
import yaml

# chrome --remote-debugging-port=9222

class TestWework:
  # 复用浏览器
    def test_demo(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_id("menu_contacts").click()
        print(driver.get_cookies())



# 使用cookie登录
def test_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    cookies =[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852552525345'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852552525345'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '245427840'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '4588141568'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325024045567'}, {'domain': '.qq.com', 'expiry': 1608358625, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2063148380.1608206121'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'r5h6wIMHO4Qkza1bxLkQC4Eg1NIi1uscPOUPM9OZZNwORXovHYDASGATnp8Cqtf9'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a295145'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2185153660995713'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608287228, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '12knpbn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610864225, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1671344225, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1560282881.1608206121'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639742113, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1609324912, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o0747781153'}, {'domain': '.qq.com', 'expiry': 1608272255, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'PNw8dSdDGOS-6gYY_VYakyO1LBP73j3LTrgVzsGQkRRdriYOhsB6kN_cz03n4SS5YvWZJbFxwz5MxAAy7qVR5TOvmdLM2t5w0QQsMJrZhjD3bUmd-5oq9inTKqS1GgGWNM0k53KNtJd9M32yoD7G2Gj2qspHD-MLJNbkeL-vGcwDFxNJCnk3ZrxWZcNwR11r9w7bDwrmsoPx64dAqC-psj5Qw5s_p4413qb3HIcYrAPiCtLrzqInM2Tj-c17m6iMksA9d8fF5vO_sDcyNV-Npw'}, {'domain': '.qq.com', 'expiry': 1921202701, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_747781153'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639742120, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608206120'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '5676e95bd340316949fb0151844a05ed0c1ce1acf76a3d98d4d3ff0882c6be9f'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '747781153'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'DBLVt/kTMD'}, {'domain': '.qq.com', 'expiry': 1609324912, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '0001000045cb72bc690e34a4845aada2527492a64a16ce97255b5b91aaffbbb2e5d78f9e53645f498af6c015'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    time.sleep(5)
    driver.quit()

# 获取cookie，序列化后存入yaml文件内
def test_get_cookie():
    opt = webdriver.ChromeOptions()
    # 设置debug地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = driver.get_cookies()
    print(cookie)
    with open("data.yaml","w",encoding="UTF-8") as f:
        yaml.dump(cookie,f)

# 使用序列化cookie的方法进行登录
def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml",encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
      driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(10)