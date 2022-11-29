import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiAccount(G1APIBase):

    @allure.step('Смена пароля пользователя. POST api/Account/ChangePassword')
    def post_account_change_password(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Account/ChangePassword', body, params)

    @allure.step('Установка пароля пользователя, если он не был ранее установлен. POST api/Account/SetPassword')
    def post_account_set_password(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Account/SetPassword', body, params)

    @allure.step('Регистрирует существующего пользователя СУ Гандива в API. POST api/Account/RegisterApi')
    def post_account_register_api(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Account/RegisterApi', body, params)

    @allure.step('Отправляет повторный запрос на подтверждение регистрации. POST api/Account/ConfirmRegistration')
    def post_account_confirm_registration(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Account/ConfirmRegistration', body, params)

    @allure.step('Восстановление пароля. POST api/Account/Restore')
    def post_account_restore(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Account/Restore', body, params)

    @allure.step('Подтверждение регистрации пользователя. GET api/Account/ConfirmEmail')
    def get_account_confirm_email(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Account/ConfirmEmail', params)

    @allure.step('Подтверждение сброса пароля. GET api/Account/ConfirmResetPassword')
    def get_account_confirm_reset_password(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Account/ConfirmResetPassword', params)
