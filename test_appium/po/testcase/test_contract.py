from test_appium.po.page.main_page import MainPage


def test_add_member():
    main = MainPage()
    main.goto_address().click_addmember().add_member_menual().add_contract()