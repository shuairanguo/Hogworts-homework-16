from test_frame.app import App


class TestSearch:
    def setup(self):
        self.app = App().start()

    def test_search(self):
        self.app.goto_main().goto_market().goto_search().search()
