import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Элементы (дополнительные поля) микросправочников.')
class TestApiCustomFields(G1ApiBase):

    @allure.title('POST api/CustomFields/SearchType')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_custom_fields_search_type(self):
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
        custom_field_search = self.APP.g1_api_custom_fields.post_custom_fields_search_type(body)
        assert self.APP.group_data.response.status_code == 200
        assert custom_field_search['Limits']['Page'] == 1
        assert custom_field_search['Limits']['PageSize'] == 2
        assert 'Data' in custom_field_search
        assert 'TotalCount' in custom_field_search

    @allure.title('POST api/CustomFields/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_custom_fields_search(self):
        body = {"Limits": {"Page": 1, "PageSize": 2}, "Order": {"Property": "Id", "DirectionType": 0}}
        custom_field_search = self.APP.g1_api_custom_fields.post_custom_fields_search(body)
        assert self.APP.group_data.response.status_code == 200
        assert custom_field_search['Limits']['Page'] == 1
        assert custom_field_search['Limits']['PageSize'] == 2
        assert 'Data' in custom_field_search
        assert 'TotalCount' in custom_field_search

    @allure.title('POST api/CustomFields')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_custom_fields(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        body = {"Limits": {"Page": 1, "PageSize": 2}, "Order": {"Property": "Id", "DirectionType": 0}}
        custom_field_search_type = self.APP.g1_api_custom_fields.post_custom_fields_search_type(body)

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        body = {
            "CustomFieldTypeId": custom_field_search_type['Data'][0]['Id'],
            "Name": "TestCustomFields AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S(),
            "Description": 'TestDescription AutomationApiTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S(),
            "IsActual": True,
        }
        create_custom_field = self.APP.g1_api_custom_fields.post_custom_fields(body)
        assert self.APP.group_data.response.status_code == 200
        assert create_custom_field['CustomFieldTypeId'] == custom_field_search_type['Data'][0]['Id']
        assert 'Id' in create_custom_field
        assert 'IsActual' in create_custom_field

    @allure.title('PUT api/CustomFields/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_custom_fields_id(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        custom_field_search_type = self.APP.g1_api_custom_fields.post_custom_fields_search_type(
            {"Limits": {"Page": 1, "PageSize": 2}, "Order": {"Property": "Id", "DirectionType": 0}})
        custom_field_search = self.APP.g1_api_custom_fields.post_custom_fields_search(
            {"Limits": {"Page": 1, "PageSize": 2}, "Order": {"Property": "Id", "DirectionType": 0}})
        name = "TestCustomFields AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationApiTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        body = {
            "CustomFieldTypeId": custom_field_search_type['Data'][0]['Id'],
            "Name": name,
            "Description": description,
            "IsActual": True,
        }
        change_custom_field = self.APP.g1_api_custom_fields.put_custom_fields_id(custom_field_search['Data'][0]['Id'], body)
        assert self.APP.group_data.response.status_code == 200
        assert change_custom_field['Id'] == custom_field_search['Data'][0]['Id']
        assert change_custom_field['CustomFieldTypeId'] == custom_field_search_type['Data'][0]['Id']
        assert change_custom_field['Name'] == name
        assert change_custom_field['Description'] == description
        assert 'Approvers' in change_custom_field
        assert 'Observers' in change_custom_field
        assert 'IsActual' in change_custom_field

    test_data = [True, False]

    @allure.title('POST api/CustomFields/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.parametrize("is_actual", test_data)
    def test_post_custom_fields_id_is_actual(self, is_actual):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
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
        custom_field_search = self.APP.g1_api_custom_fields.post_custom_fields_search(body)
        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        change_custom_field = self.APP.g1_api_custom_fields.post_custom_fields_id_is_actual(custom_field_search['Data'][0]['Id'], {'IsActual': is_actual})
        assert self.APP.group_data.response.status_code == 200
        assert change_custom_field['Id'] == custom_field_search['Data'][0]['Id']
        assert 'CustomFieldTypeId' in change_custom_field
        assert 'Name' in change_custom_field
        assert 'Description' in change_custom_field
        assert 'Approvers' in change_custom_field
        assert 'Observers' in change_custom_field
        assert change_custom_field['IsActual'] == is_actual