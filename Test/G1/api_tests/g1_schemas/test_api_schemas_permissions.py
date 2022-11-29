import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Разрешения на операции в системе.')
class TestApiSchemasPermissions(G1ApiBase):

    @allure.title('GET api/Permissions/Request/New')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_permissions_request_new(self):
        request = self.APP.g1_api_permissions.get_permissions_request_new()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int

    @allure.title('GET api/Permissions/Request/Edit/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_permissions_request_edit_id(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем разрешения
        request = self.APP.g1_api_permissions.get_permissions_request_edit_id(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int

    @allure.title('GET api/Permissions/Task/New')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_permissions_task_new(self):
        request = self.APP.g1_api_permissions.get_permissions_task_new()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int

    @allure.title('GET api/Permissions/Task/Edit/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_permissions_task_edit_id(self):
        # Создаем заявку
        request = self.g1_create_task()
        # Получаем разрешения
        request = self.APP.g1_api_permissions.get_permissions_task_edit_id(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int