import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Custom Field Dictionary')
@allure.story('Добавление значения в пользовательском справочнике')
class TestAddValueCustomFieldDictionary(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    @allure.title('Добавление значения в пользовательский справочник через кнопку Добавить значение')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_add_value_a_custom_field_dictionary_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Получаем количество записей в справочнике до добавления
        count_1 = self.APP.web_custom_field_dictionary.get_count_values()
        # Добавляем значение в пользовательский справочник через кнопку Добавить значение
        self.APP.web_custom_field_dictionary.add_value_a_custom_field_dictionary_first()
        # Получаем количество записей в справочнике после добавления
        count_2 = self.APP.web_custom_field_dictionary.get_count_values()
        assert count_2 - count_1 == 1

    @allure.title('Добавление значения в пользовательский справочник через ПКМ на строку и кнопку Добавить значение')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_add_value_a_custom_field_dictionary_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Получаем количество записей в справочнике до добавления
        count_1 = self.APP.web_custom_field_dictionary.get_count_values()
        # Добавляем значение в пользовательский справочник через ПКМ на строку и кнопку Добавить значение
        self.APP.web_custom_field_dictionary.add_value_a_custom_field_dictionary_second()
        # Получаем количество записей в справочнике после добавления
        count_2 = self.APP.web_custom_field_dictionary.get_count_values()
        assert count_2 - count_1 == 1

    @allure.title('Добавление значения в пользовательский справочник через кнопку Добавить, когда справочник пуст')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_add_value_a_custom_field_dictionary_third(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_пустой_справочник_01.01.0101'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Удаляем все строки в справочнике если они есть
        self.APP.web_custom_field_dictionary.delete_all_value_a_custom_field_dictionary()
        # Получаем количество записей в справочнике до добавления
        count_1 = self.APP.web_custom_field_dictionary.get_count_values()
        # Добавляем значение в пользовательский справочник через кнопку Добавить, когда справочник пуст
        self.APP.web_custom_field_dictionary.add_value_a_custom_field_dictionary_third()
        # Получаем количество записей в справочнике после добавления
        count_2 = self.APP.web_custom_field_dictionary.get_count_values()
        assert count_2 - count_1 == 1
