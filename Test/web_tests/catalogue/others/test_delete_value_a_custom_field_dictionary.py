import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Custom Field Dictionary')
@allure.story('Удаление значения в пользовательском справочнике')
class TestDeleteValueCustomFieldDictionary(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    @allure.title('Удаление значения в пользовательском справочнике через ПКМ на строку и кнопку Удалить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_delete_value_a_custom_field_dictionary_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Получаем количество записей в справочнике до удаления
        count_1 = self.APP.web_custom_field_dictionary.get_count_values()
        # Удаляем значение из пользовательского справочника
        self.APP.web_custom_field_dictionary.delete_value_first()
        # Получаем количество записей в справочнике после удаления
        count_2 = self.APP.web_custom_field_dictionary.get_count_values()
        assert count_1 - count_2 == 1

    @allure.title('Удаление значения в пользовательском справочнике через ПКМ на строку и кнопку Изменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_delete_value_a_custom_field_dictionary_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Получаем количество записей в справочнике до удаления
        count_1 = self.APP.web_custom_field_dictionary.get_count_values()
        # Удаляем значение из пользовательского справочника
        self.APP.web_custom_field_dictionary.delete_value_second()
        # Получаем количество записей в справочнике после удаления
        count_2 = self.APP.web_custom_field_dictionary.get_count_values()
        assert count_1 - count_2 == 1


