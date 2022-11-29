import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Заявки. Работа с доп. полями.')
class TestApiCustomFieldInTheRequest(ApiBase):

    @allure.title('Создание заявки с услугой, в которой предусмотрены доп. поля')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_request_with_service_custom_field(self):
        # Создаем заявку с услугой, в которой предусмотрены доп. поля
        request = self.create_request_with_custom_fields('AutomationService Тестовый Тип 14')
        # Получаем список доп. полей в заявке
        request_custom_field_list = self.APP.api_request_custom_field_collection.get_request_custom_field_collection_id(request['id'])
        assert request['hasCustomFields']
        assert request_custom_field_list[0]['name'] == 'Текст'
        assert request_custom_field_list[1]['name'] == 'Дата'
        assert request_custom_field_list[2]['name'] == 'Справочник "Пользователи"'

    test_data = ['Text', 'Date', 'UserDictionary']

    @allure.title('Редактирование значения доп. поля в заявке от лица инициатора')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('custom_field_type', test_data)
    def test_edit_custom_field_in_request_by_initiator(self, custom_field_type):
        # Создаем заявку с услугой, в которой предусмотрены доп. поля
        request = self.create_request_with_custom_fields('AutomationService Тестовый Тип 14')
        # Получаем список доп. полей в заявке
        request_custom_field_list = self.APP.api_request_custom_field_collection.get_request_custom_field_collection_id(
            request['id'])
        number_in_list = 0
        if custom_field_type == 'Text':
            number_in_list = 0
            value = 'AutomationApiTest'
        elif custom_field_type == 'Date':
            number_in_list = 1
            value = '2022-07-18T00:00:00Z'
        elif custom_field_type == 'UserDictionary':
            number_in_list = 2
            value = {'id': self.APP.group_data.users['test_user01']['user_id']}
        # Обновляем значение текстового поля
        custom_field = self.APP.api_actions_in_request_with_custom_field.edit_values_in_custom_field_from_request(request_custom_field_list[number_in_list]['id'], custom_field_type, value)
        assert custom_field['customField']['name'] == request_custom_field_list[number_in_list]['name']
        assert custom_field['customField']['id'] == request_custom_field_list[number_in_list]['id']
        assert custom_field['customField']['data']['type'] == request_custom_field_list[number_in_list]['data']['type']
        if custom_field_type == 'Text' or custom_field_type == 'Date':
            assert custom_field['customField']['data']['value'] == value
        elif custom_field_type == 'UserDictionary':
            assert custom_field['customField']['data']['value']['id'] == self.APP.group_data.users['test_user01']['user_id']

            