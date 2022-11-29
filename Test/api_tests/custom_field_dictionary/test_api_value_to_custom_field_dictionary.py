import allure
import pytest

from Test.api_tests.api_base import ApiBase

@allure.feature('Api - Value To Custom Field Dictionary')
@allure.story('Добавление, редактирование, удаление значения в пользовательских справочниках')
class TestApiValueToCustomFieldDictionary(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    @allure.title('Добавление значений в пользовательский справочник')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_add_value_to_custom_field_dictionary(self):

        # Создаем пользовательский справочник
        create_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.create_custom_field_dictionary()

        # Создаем название значению
        value_text = 'Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Добавляем значение в пользовательский справочник
        add_value_to_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.add_value_to_custom_field_dictionary(create_custom_field_dictionary['id'], create_custom_field_dictionary['customFields'][0]['id'], value_text)

        # Получаем количество созданных значений в пользовательском справочнике
        list_value = self.APP.api_actions_in_custom_field_dictionary.search_value_to_custom_field_dictionary(create_custom_field_dictionary['id'])

        # Проверяем количество созданных значений с ожидаемым
        assert list_value['totalCount'] == 1
        # Проверяем название значения с ожидаемым
        assert add_value_to_custom_field_dictionary[0]['customFields'][0]['value'] == value_text

    @allure.title('Удаление нужного значения в пользовательском справочнике')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_value_to_custom_field_dictionary(self):
        # Создаем пользовательский справочник
        create_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.create_custom_field_dictionary()

        # Добавляем 2 значения в пользовательский справочник, для проверки удаления необходимого значения
        list_add_value = []
        for i in range(2):
            value = self.APP.api_actions_in_custom_field_dictionary.add_value_to_custom_field_dictionary(create_custom_field_dictionary['id'], create_custom_field_dictionary['customFields'][0]['id'])
            list_add_value.append(value[0]['rowId'])

        # Удаляем выбранное значение (1й по списку) в пользовательском справочнике
        self.APP.api_actions_in_custom_field_dictionary.delete_value_to_custom_field_dictionary(create_custom_field_dictionary['id'],  list_add_value[0])

        # Получаем список значений в пользовательском справочнике
        list_value = self.APP.api_actions_in_custom_field_dictionary.search_value_to_custom_field_dictionary(create_custom_field_dictionary['id'])

        # Получаем отдельный список из id значений
        list_id_value = self.APP.api_actions_in_custom_field_dictionary.search_id_value_to_custom_field_dictionary(create_custom_field_dictionary['id'])

        # Проверяем количество значений с ожидаемым (1 значение)
        assert list_value['totalCount'] == 1
        # Проверяем удаление выбронного значения по id (1й по списку)
        assert list_add_value[0] not in list_id_value

    @allure.title('Редактирование значений в пользовательском справочнике')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_edit_value_to_custom_field_dictionary(self):
        # Создаем пользовательский справочник
        create_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.create_custom_field_dictionary()

        # Добавляем значение в пользовательский справочник
        add_value_to_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.add_value_to_custom_field_dictionary(create_custom_field_dictionary['id'], create_custom_field_dictionary['customFields'][0]['id'])

        # Записываем в переменную новый текст для редактирования значения в пользовательском справочнике
        new_value_text = 'NewText AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Редактируем значение в пользовательском справочнике
        edit_value_to_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.edit_value_to_custom_field_dictionary(create_custom_field_dictionary['id'],  create_custom_field_dictionary['customFields'][0]['id'], add_value_to_custom_field_dictionary[0]['rowId'], new_value_text)

        # Проверяем изменение значения на новый текст
        assert new_value_text == edit_value_to_custom_field_dictionary[0]['customFields'][0]['value']