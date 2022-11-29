import allure

from Test.test_base import TestBase


class WebBase(TestBase):

    def setup_class(self):
        self.APP.web_any_page.open_main_page()

    def setup_method(self):
        self.APP.web_any_page.open_main_page()

    def teardown_method(self):
        self.APP.web_any_page.allure_screenshot()

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

