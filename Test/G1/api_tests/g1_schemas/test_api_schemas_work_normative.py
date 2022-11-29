import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Норматив.')
class TestApiSchemasWorkNormative(G1ApiBase):

    @allure.title('GET api/workNormative/departments')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_departments(self):
        request = self.APP.g1_api_work_normative.get_work_normative_departments()
        assert self.APP.group_data.response.status_code == 200
        assert request
        assert 'Id' in request[0]
        assert 'Name' in request[0]

    @allure.title('GET api/workNormative/departments/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_departments_id(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_work_normative.get_work_normative_departments_id(normative[0]['Department']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert 'Name' in request
        assert request['Id'] == normative[0]['Department']['Id']

    @allure.title('GET api/workNormative/departments/departmentId/categories')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_departments_department_id_categories(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_work_normative.get_work_normative_departments_department_id_categories(normative[0]['Department']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert request
        assert 'Id' in request[0]
        assert 'DepartmentId' in request[0]
        assert 'Name' in request[0]

    @allure.title('GET api/workNormative/categories/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_categories_id(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_work_normative.get_work_normative_categories_id(normative[0]['Category']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'DepartmentId' in request
        assert 'Name' in request

    @allure.title('GET api/workNormative/categories/categoryId/requestTypes')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_categories_category_id_request_types(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_work_normative.get_work_normative_categories_category_id_request_types(normative[0]['Category']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert request
        assert 'Id' in request[0]
        assert 'CategoryId' in request[0]
        assert 'Name' in request[0]

    @allure.title('GET api/workNormative/requestTypes/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_request_types_id(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_work_normative.get_work_normative_request_types_id(normative[0]['RequestType']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'CategoryId' in request
        assert 'Name' in request

    @allure.title('GET api/workNormative/requestTypes/requestTypeId/jobTypes')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_request_types_request_type_id_job_types(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_work_normative.get_work_normative_request_types_request_type_id_job_types(normative[0]['RequestType']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert request
        assert 'Id' in request[00]
        assert 'RequestTypeId' in request[00]
        assert 'Name' in request[00]

    @allure.title('GET api/workNormative/jobTypes/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_job_types_id(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})
        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()
        request = self.APP.g1_api_work_normative.get_work_normative_job_types_id(normative[0]['JobType']['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'RequestTypeId' in request
        assert 'Name' in request

    @allure.title('GET api/workNormative/CustomFields')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_custom_fields(self):
        request = self.APP.g1_api_work_normative.get_work_normative_custom_fields(params={'departmentId': 38, 'categoryId': 489, 'requestTypeId': 2552, 'jobTypeId': 13729})
        assert self.APP.group_data.response.status_code == 200
        assert "Permissions" in request[0]
        assert "WorkNormativeId" in request[0]
        assert "CustomFieldId" in request[0]
        assert "CustomFieldType" in request[0]
        assert "Name" in request[0]
        assert "Order" in request[0]
        assert "Required" in request[0]
        assert "CustomFieldRequiredRoleId" in request[0]

    @allure.title('GET api/workNormative/id/CustomFields')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_id_custom_fields(self):
        request = self.APP.g1_api_work_normative.get_work_normative_id_custom_fields(id=4202)
        assert self.APP.group_data.response.status_code == 200
        assert "Permissions" in request[0]
        assert "WorkNormativeId" in request[0]
        assert "CustomFieldId" in request[0]
        assert "CustomFieldType" in request[0]
        assert "Name" in request[0]
        assert "Order" in request[0]
        assert "Required" in request[0]
        assert "CustomFieldRequiredRoleId" in request[0]

    @allure.title('GET api/workNormative/CustomFields/id/Dictionary')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_custom_fields_id_dictionary(self):
        request = self.APP.g1_api_work_normative.get_work_normative_custom_fields_id_dictionary(id=4202)
        assert self.APP.group_data.response.status_code == 200
        assert "Value" in request[0]
        assert "Text" in request[0]

    @allure.title(' GET api/workNormative/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_work_normative_search(self):
        request = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': "test", 'size': 1, 'page': 1, 'any': True})
        assert self.APP.group_data.response.status_code == 200
        assert "Id" in request[0]
        assert "Department" in request[0]
        assert "Category" in request[0]
        assert "RequestType" in request[0]
        assert "JobType" in request[0]

    @allure.title('POST api/workNormative/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Нуров Владимир Муратович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_work_normative_search(self):
        body = {
            "Limits": {
                "Page": 1,
                "PageSize": 2
            },
            "Order": {
                "Property": "Id",
                "DirectionType": 0
            }
        }

        request = self.APP.g1_api_work_normative.post_work_normative_search(body=body)
        assert self.APP.group_data.response.status_code == 200
        assert 'TotalCount' in request
        assert 'Data' in request
