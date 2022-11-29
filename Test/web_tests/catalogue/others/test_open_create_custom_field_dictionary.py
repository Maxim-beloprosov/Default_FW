import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Custom Field Dictionary')
@allure.story('Переходы к созданию пользовательских справочников')
class TestOpenCreateCustomFieldDictionary(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    correct_title_pop_up_block_create_custom_field_dictionary = {
        'correct_title_rus': 'Создание справочника',
        'correct_title_eng': 'Creating a directory'
    }

    @allure.title('Переход к созданию пользовательского справочника через кнопку Создать справочник')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_custom_field_dictionary_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Нажимаем на кнопку Создать справочник
        self.APP.web_custom_field_dictionary.button_create_catalogue()
        # Возвращаем заголовок всплывающего окна
        actual_title = self.APP.web_custom_field_dictionary.get_title_pop_up_block()
        # Сравниваем 2 заголовка между собой
        assert actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_rus'] or actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_eng']

    @allure.title('Переход к созданию пользовательского справочника через кнопку создайте новый')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_custom_field_dictionary_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Нажимаем на кнопку создайте новый
        self.APP.web_custom_field_dictionary.button_create_new()
        # Возвращаем заголовок всплывающего окна
        actual_title = self.APP.web_custom_field_dictionary.get_title_pop_up_block()
        # Сравниваем 2 заголовка между собой
        assert actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_rus'] or actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_eng']

    @allure.title('Переход к созданию пользовательского справочника через кнопку Добавить в дереве')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_custom_field_dictionary_third(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Нажимаем на кнопку Добавить
        self.APP.web_custom_field_dictionary.button_add_in_tree()
        # Возвращаем заголовок всплывающего окна
        actual_title = self.APP.web_custom_field_dictionary.get_title_pop_up_block()
        # Сравниваем 2 заголовка между собой
        assert actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_rus'] or actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_eng']

    @allure.title('Переход к созданию пользовательского справочника через ПКМ на дерево и кнопку Добавить справочник')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_custom_field_dictionary_fourth(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Нажимаем правой кнопкой на дерево и дальше нажимаем кнопку "Добавить справочник"
        self.APP.web_custom_field_dictionary.button_add_catalogue_in_pop_up_block_in_tree()
        # Возвращаем заголовок всплывающего окна
        actual_title = self.APP.web_custom_field_dictionary.get_title_pop_up_block()
        # Сравниваем 2 заголовка между собой
        assert actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_rus'] or actual_title == self.correct_title_pop_up_block_create_custom_field_dictionary['correct_title_eng']

