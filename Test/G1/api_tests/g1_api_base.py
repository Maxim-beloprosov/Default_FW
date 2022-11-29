import allure

from Test.test_base import TestBase


class G1ApiBase(TestBase):

    def setup_class(self):
        pass

    def setup_method(self):
        self.APP.g1_api_token.get_token()

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass
