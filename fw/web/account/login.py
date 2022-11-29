import allure
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from fw.web.AnyPage import AnyPage


class Locator:
    local_form = (By.XPATH, '//div[@test_id="local-form"]')
    input_login = (By.XPATH, '//input[@test_id="local-login-input"]')
    input_password = (By.XPATH, '//input[@test_id="local-password-input"]')
    select_local_form = (By.XPATH, '//a[@test_id="adsf-sign-in"]')
    local_submit_button = (By.XPATH, '//*[@test_id="local-submit-button"]')


class Login(AnyPage):

    @allure.step('Вход по логину и паролю')
    def user_authorization(self, user_data):
        if self.checking_url_for_authorization():
            self.login_log_pas(user_data['Login'], user_data['Password'])
        else:
            correct_surname_and_name = user_data['Surname'] + ' ' + user_data['Name']
            actual_surname_and_name = self.get_surname_and_name_autorizated_user()
            if actual_surname_and_name != correct_surname_and_name:
                self.change_user(user_data['Login'], user_data['Password'])

    @allure.step('Вход по логину и паролю')
    def login_log_pas(self, login, password):
        self.click_element(Locator.local_form)
        self.send_keys(Locator.input_login, login)
        self.send_keys(Locator.input_password, password)
        self.click_element(Locator.local_submit_button)
        self.manager.web_activity.page_loaded()
        return self.manager.web_activity

    @allure.step('Вход через AD')
    def login_ad(self):
        self.click_element(Locator.select_local_form)
        self.manager.web_activity.page_loaded()
        return self.manager.web_activity

    def checking_url_for_authorization(self):
        url = self.get_current_url()
        if ('Account' in url) and ('Login' in url):
            return True
        else:
            return False
