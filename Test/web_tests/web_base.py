import allure

from Test.test_base import TestBase


class WebBase(TestBase):

    def setup_class(self):
        self.users = self.APP.group_data.users
        self.APP.scripts_users.update_users_settings(take_non_updatable_keys=True)
        self.APP.web_any_page.open_main_page()
        self.APP.web_login.user_authorization(self.users['test_user09'])
        self.status_ticket = self.APP.group_data.Status_ticket
        # self.APP.api_token.get_token('test_user09')

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_login.user_authorization(self.users['test_user09'])
        self.APP.api_token.get_token('test_user09')

    def teardown_method(self):
        self.APP.web_any_page.allure_screenshot()

    def teardown_class(self):
        self.APP.driver_instance.stop_driver()

    def create_task_in_web(self, name=None, description=None, contractor=None):
        if name is None: name = "TestTask AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        if description is None: description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        if contractor is None: contractor = self.users['test_user01']['Surname'] + ' ' + self.users['test_user01']['Name']

        self.APP.web_any_page.click_btn_create_task_left_menu()
        self.APP.web_tickets_base.fill_name(name)
        self.APP.web_tickets_base.fill_description_in_ticket(description)
        self.APP.web_tickets_base.add_contractor(contractor)
        self.APP.web_task_create.click_button_to_create_task()
        return name, description, contractor
