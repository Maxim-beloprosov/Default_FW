import allure
import csv

from Test.test_base import TestBase


class TestStressTestingScripts(TestBase):

    @allure.title('НЕ ТЕСТ! скрипт создания CSV файла для нагрузочного тестирования')
    def test_temp2(self):
        body = {
            "accountInputStatus": "Active",
            "skip": 600,
            "take": 400,
        }
        users_filter = self.APP.api_users.post_users_filter(body)
        print(f"Найдено пользователей - {len(users_filter['items'])}")
        with open('users_token.csv', 'w', newline='') as csv_file:
            fail_user = 0
            pass_user = 0
            csv_writer = csv.writer(csv_file, delimiter=',')
            for user in users_filter['items']:
                line = []
                line.append(user['id'])
                # Запросить все ключи с сервера
                secrets_list = self.APP.api_users.get_users_user_id_secrets(user['id'])

                if len(secrets_list) == 0:
                    body_secret = {
                        "name": f"{user['login']} {self.APP.time.get_date_Users_API()}",
                        "expireTime": f"{self.APP.time.get_date_time_for_api_g2(365)}"
                    }
                    secrets_response = self.APP.api_users.post_users_user_id_secrets(user['id'], body_secret)
                else:
                    secrets_response = self.APP.api_users.post_users_user_id_secrets_secret_id(secrets_list[0]['userId'], secrets_list[0]['secretId'], {})

                try:
                    res = self.APP.api_token.get_token_for_user(client_id=secrets_response['userId'], client_secret=secrets_response['secret'])
                    line.append(res['access_token'].rstrip())
                    csv_writer.writerow(line)
                    pass_user += 1
                except:
                    fail_user += 1
        print(f"Количество успешно добавленных - {pass_user}")
        print(f"Количество ошибок - {fail_user}")

    @allure.title('НЕ ТЕСТ! ')
    def test_temp3(self):
        # получить список услуг
        body = {
            "skip": 0,
            "take": 1000,
            "filter": {
                "serviceTypes": [
                    "Normal"
                ],
                "type": "Service"
            },
            "isActive": True,
        }
        service_list = self.APP.api_service_catalogs.post_service_catalogs_filter_list(body)
        with open('service_id_list.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')

            for service in service_list['items']:
                line = []
                line.append(service['id'])
                line.append('temp')
                try:
                    csv_writer.writerow(line)
                except:
                    pass
