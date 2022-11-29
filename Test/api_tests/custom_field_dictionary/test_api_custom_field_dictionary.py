import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Custom Field Dictionary')
@allure.story('Создание, редактирование, удаление пользовательских справочников')
class TestApiCustomFieldDictionary(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    @allure.title('Создание пользовательского справочника')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_custom_field_dictionary(self):
        # Создаем пользовательский справочник
        create_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.create_custom_field_dictionary()

        custom_field_dictionary_id = create_custom_field_dictionary['id']

        assert create_custom_field_dictionary['id'] == custom_field_dictionary_id

    @allure.title('Редактирование пользовательского справочника')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_change_custom_field_dictionary(self):
        # Создаем пользовательский справочник
        create_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.create_custom_field_dictionary()

        # Записываем в переменную новое название для пользовательского справочника
        changed_name = 'AutoTest '
        is_active = True

        # Редактируем поля пользовательского справочника
        custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.change_custom_field_dictionary(
            create_custom_field_dictionary, changed_name, is_active)

        assert changed_name in custom_field_dictionary['name']
        assert custom_field_dictionary['isActive'] == is_active

    @allure.title('Удаление пользовательского справочника')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_custom_field_dictionary(self):
        # Создаем пользовательский справочник
        create_custom_field_dictionary = self.APP.api_actions_in_custom_field_dictionary.create_custom_field_dictionary()

        # Удаляем пользовательский справочник
        custom_field_dictionary = self.APP.api_custom_field_dictionary.delete_custom_field_dictionary(
            create_custom_field_dictionary['id'])

        assert custom_field_dictionary['isDeleted'] == True

    # TODO Добавить тесты
    # TODO Добавление значений в пользовательский справочник
    # TODO Удаление значений в пользовательском справочнике
    # TODO Редактирование значений в пользовательском справочнике
