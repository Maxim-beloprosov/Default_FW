from Test.test_base import TestBase


class G1WebBase(TestBase):

    def setup_class(self):
        self.users = self.APP.group_data.g1_users
        self.APP.g1_web_any_page.open_main_page()
        self.APP.g1_web_any_page.g1_change_user('user1 test')
        self.APP.g1_api_token.get_token('User1')
        self.status_ticket = self.APP.group_data.g1_Status_ticket

    def setup_method(self):
        self.APP.g1_web_any_page.open_main_page()
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user1 test')
        self.APP.g1_api_token.get_token('User1')

    def teardown_method(self):
        self.APP.web_any_page.allure_screenshot()

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()


