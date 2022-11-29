import allure
import requests

from json.decoder import JSONDecodeError
from fw.api.api_base import APIBase


class Token(APIBase):

    @allure.step('Получение токена для пользователя {user_name}. get_token')
    def get_token(self, user_name='SystemOperator'):
        """
        Метод получения АПИ токена
        :param user_name: Имя пользователя берётся из пользователей указанных в файле settings для запускаемого branch
        :return:
        """
        if user_name == 'SystemOperator':
            client_id = self.manager.settings.GLOBAL[self.manager.settings.branch]['USERS'][user_name]['User_id']
            client_secret = self.manager.settings.GLOBAL[self.manager.settings.branch]['USERS'][user_name]['client_secret']
        else:
            client_id = self.manager.group_data.users[user_name]['user_id']
            client_secret = self.manager.group_data.users[user_name]['secret']

        url = self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['AUTH_URL']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
        response = requests.post(url, headers=headers, data=body)

        self.request_logs('POST', url, str(headers), str(body), str(response.status_code), response.text)
        response = response.json()
        self.manager.group_data.access_token = response['access_token']
        self.manager.group_data.expires_in = response['expires_in']
        self.manager.group_data.token_type = response['token_type']

    @allure.step('Получение токена для пользователя')
    def get_token_for_user(self, client_id, client_secret):
        url = self.manager.settings.GLOBAL[self.manager.settings.branch]['API']['AUTH_URL']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
        response = requests.post(url, headers=headers, data=body)

        self.manager.group_data.response = response
        response = response.json()

        return response