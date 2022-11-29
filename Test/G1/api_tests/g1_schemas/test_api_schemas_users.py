import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Токен.')
class TestApiSchemasUsers(G1ApiBase):

    def teardown_method(self):
        self.APP.g1_api_users.put_users_current(body={'MobilePhone': None})

    @allure.title('GET api/Users/Id/photo')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip(reason='сервер отдает 500')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/21357')
    def test_get_users_id_photo(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Получаем фото пользователя
        request = self.APP.g1_api_users.get_users_id_photo(user01_id)
        assert request
        assert self.APP.group_data.response.status_code == 200

    @allure.title('GET api/Users/photo')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip(reason='сервер отдает 500')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/21360')
    def test_get_users_photo(self):
        # Получаем фото пользователя
        request = self.APP.g1_api_users.get_users_photo()
        assert request
        assert self.APP.group_data.response.status_code == 200

    @allure.title('GET api/Users/profile')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip(reason='Логин пользователя не совпадает с логинами на других серверах. Где то логин написан через "_", где то без "_"')
    def test_get_users_profile(self):
        # Получаем профиль пользователя
        request = self.APP.g1_api_users.get_users_profile(params={"login": self.APP.group_data.g1_users['User1']['Login']})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Email' in request
        assert 'FirstName' in request
        assert 'LastName' in request

    @allure.title('GET api/Users/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_users_id(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Получаем профиль пользователя
        request = self.APP.g1_api_users.get_users_id(user01_id)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Login' in request
        assert 'Email' in request
        assert 'FirstName' in request

    @allure.title('GET api/Users/current')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_users_current(self):
        # Получаем профиль пользователя
        request = self.APP.g1_api_users.get_users_current()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Login' in request
        assert 'Email' in request

    @allure.title('PUT api/Users/current')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_users_current(self):
        # Редактируем профиль текущего пользователя
        request = self.APP.g1_api_users.put_users_current(body={'MobilePhone': '88005553535'})
        assert request
        assert self.APP.group_data.response.status_code == 200

    @allure.title('GET api/Users/search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_users_search(self):
        # ищем сотрудника
        request = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'FirstName' in request[0]
        assert 'LastName' in request[0]
        assert 'Organization' in request[0]
        assert 'Position' in request[0]

    @allure.title('GET api/Users/ResponsibilityGroups')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_users_responsibility_groups(self):
        self.APP.g1_api_token.get_token('User1')
        # получаем ГО пользователя
        request = self.APP.g1_api_users.get_users_responsibility_groups()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'Name' in request[0]

    @allure.title('GET api/Users/Regions')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_users_regions(self):
        # получаем список регионов
        request = self.APP.g1_api_users.get_users_regions()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'Code' in request[0]
        assert 'Name' in request[0]

    @allure.title('POST api/Users/FunctioningCapacity')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_users_function_capacity(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Получаем рабочую загруженность пользователей
        request = self.APP.g1_api_users.post_users_function_capacity(body=[user01_id])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert request[0]['UserId'] == user01_id
        assert 'UserName' in request[0]

    @allure.title('PUT api/Users')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_users(self):
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Редактируем пользователя
        request = self.APP.g1_api_users.put_users(body={'Id': user01_id, 'MobilePhone': '88005553535'})
        assert request
        assert self.APP.group_data.response.status_code == 200
