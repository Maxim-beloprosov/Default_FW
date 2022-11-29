import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Лента активности.')
class TestApiSchemasActivity(G1ApiBase):

    @allure.title('GET api/Activity')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_activity(self):
        # Получаем ленту активности
        request = self.APP.g1_api_acctivity.get_activity(params={'Page': 1, 'Size': 20})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Permissions' in request[0]
        assert 'LastModifiedDate' in request[0]
        assert 'Id' in request[0]

    @allure.title('GET api/Activity/Count')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_activity_count(self):
        # Получаем кол-во непрочитанных комментариев из ленты активности
        request = self.APP.g1_api_acctivity.get_activity_count()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int

    @allure.title('GET api/Activity/Requests/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_activity_requests_id(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']
        # Получаем id инициатора
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Добавление обозревателя в заявку.
        self.APP.g1_api_actions_in_request.update_observers_in_request(request['Id'], request['LastModifiedDate'], [user02_id])
        # Перелогиниваемся на обозревателя
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')
        # пишем коммент
        self.APP.g1_api_requests.post_requests_id_comments(request['Id'], body={'Text': 'AutomationApiTest Comment', 'Addressees': [user01_id]})
        # перелогиниваемся на инициатора
        self.APP.g1_api_token.get_token()
        # Получаем заявку-элемент ленты активности
        request = self.APP.g1_api_acctivity.get_activity_requests_id(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Permissions' in request
        assert 'LastModifiedDate' in request
        assert 'Id' in request
        assert 'ActivityItemType' in request

    @allure.title('GET api/Activity/Tasks/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_activity_tasks_id(self):
        # Создаем задачу
        task = self.g1_create_task()
        # Получаем id инициатора
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'Владислав Земцов', 'kind': 'Any'})[0]['Id']
        # Перелогиниваемся на исполнителя
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')
        # пишем коммент
        self.APP.g1_api_tasks.post_tasks_id_comments(task['Id'], body={'Text': 'AutomationApiTest Comment', 'Addressees': [user01_id]})
        # перелогиниваемся на инициатора
        self.APP.g1_api_token.get_token(login='agat\\v.zemtsov', password='Subwoofer100123077')
        # Получаем задачу-элемент ленты активности
        task = self.APP.g1_api_acctivity.get_activity_tasks_id(task['Id'])
        assert task
        assert self.APP.group_data.response.status_code == 200
        assert 'Permissions' in task
        assert 'LastModifiedDate' in task
        assert 'Id' in task
        assert 'ActivityItemType' in task
        assert 'Status' in task
        assert 'Description' in task
        assert 'AccessRequest' in task
        assert 'Comments' in task