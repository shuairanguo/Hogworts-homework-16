from test_frame.base_page import BasePage
from test_frame.page.market import Market
from test_frame.page.pre_page import PrePage


class MainPage(PrePage):

    def goto_market(self):
        self.basepage.load('../page/main.yaml')
        return Market(self.basepage)
