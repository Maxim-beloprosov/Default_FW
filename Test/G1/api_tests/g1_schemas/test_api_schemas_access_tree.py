import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Ресурсы допуска.')
class TestApiSchemasAccessTree(G1ApiBase):

    @allure.title('POST api/AccessTree/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_access_tree_search(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        body = {'ApproverIds': [user01_id, user02_id],
                'Limits': {'Page': 1, 'PageSize': 10},
                'Order': {'Property': 'Name', 'DirectionType': 1}}
        # Запрос на поиск
        request = self.APP.g1_api_access_tree.post_access_tree_search(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Limits' in request
        assert 'TotalCount' in request
        assert 'Data' in request

    @allure.title('GET api/AccessTree/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_access_tree_id(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        body = {'ApproverIds': [user01_id, user02_id],
                'Limits': {'Page': 1, 'PageSize': 10},
                'Order': {'Property': 'Name', 'DirectionType': 1}}
        # ищем нужный ресурс допуска
        access_tree = self.APP.g1_api_access_tree.post_access_tree_search(body)
        # получаем ресурс допуска по id
        request = self.APP.g1_api_access_tree.get_access_tree_id(access_tree['Data'][0]['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert request['Id'] == access_tree['Data'][0]['Id']
        assert 'Name' in request
        assert 'IsActual' in request
        assert 'Parent' in request
        assert 'Approvers' in request
        assert 'WorkNormative' in request

    @allure.title('GET api/AccessTree/ChildrenNodes/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_access_tree_children_nodes_id(self):
        # получаем дерево ресурсов допуска
        request = self.APP.g1_api_access_tree.get_access_tree_children_nodes_id('')
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'ParentId' in request[0]
        assert 'Name' in request[0]
        assert 'Approvers' in request[0]
        assert 'ExistChildren' in request[0]
        assert 'PlanTimeExecution' in request[0]

    @allure.title('POST api/AccessTree')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_access_tree(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        body = {'ApproverIds': [user01_id, user02_id],
                'Limits': {'Page': 1, 'PageSize': 10},
                'Order': {'Property': 'Name', 'DirectionType': 1}}
        # ищем нужный ресурс допуска
        access_tree = self.APP.g1_api_access_tree.post_access_tree_search(body)
        # получаем ресурс допуска по id
        access_tree = self.APP.g1_api_access_tree.get_access_tree_id(access_tree['Data'][0]['Id'])
        # Тело для создания ресурса допуска
        body = {'Name': 'AutomationApiTest ' + self.APP.time.get_time_now(),
                'DepartmentId': access_tree['WorkNormative']['Department']['Id'],
                'CategoryId': access_tree['WorkNormative']['Category']['Id'],
                'RequestTypeId': access_tree['WorkNormative']['RequestType']['Id'],
                'JobTypeId': access_tree['WorkNormative']['JobType']['Id'],
                'Approvers': [user01_id, user02_id]}
        # Создаем ресурс допуска
        request = self.APP.g1_api_access_tree.post_access_tree(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Name' in request
        assert 'IsActual' in request
        assert 'Parent' in request
        assert 'Approvers' in request
        assert 'WorkNormative' in request
        