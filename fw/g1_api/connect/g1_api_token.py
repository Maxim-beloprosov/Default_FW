import allure
import requests

from fw.api.api_base import APIBase


class G1ApiToken(APIBase):

    @allure.step('Получение токена для пользователя {user_name}. get_token')
    def get_token(self, user_name='SystemOperator', login=None, password=None):
        """
        Метод получения АПИ токена
        :param user_name: Имя пользователя берётся из пользователей указанных в файле settings для запускаемого branch
        :return:
        """

        url = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['API']['AUTH_URL']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        if (login is not None) and (password is not None):
            body = {'grant_type': 'password', 'username': login, 'password': password}
        else:
            if user_name == 'SystemOperator':
                login = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['USERS']['SystemOperator']['ApiLogin']
                password = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['USERS']['SystemOperator']['Password']
                body = {'grant_type': 'password', 'username': login, 'password': password}
            else:
                login = self.manager.group_data.g1_users[user_name]['Email']
                password = self.manager.group_data.g1_users[user_name]['Password']
                body = {'grant_type': 'password', 'username': login, 'password': password}

        response = requests.post(url, headers=headers, data=body)

        self.request_logs('POST', url, str(headers), str(body), str(response.status_code), response.text)

        response = response.json()
        self.manager.group_data.access_token = response['access_token']
        self.manager.group_data.token_type = response['token_type']
        self.manager.group_data.refresh_token = response['refresh_token']
        return response
