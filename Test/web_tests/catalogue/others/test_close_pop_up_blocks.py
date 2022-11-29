import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Custom Field Dictionary')
@allure.story('Закрытие всплывающих окон')
class TestClosePopUpBlock(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    @allure.title('Закрыть окно Создание справочника через крестик')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_creating_catalogue_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Переходим к созданию справочника
        self.APP.web_custom_field_dictionary.button_create_catalogue()
        # Нажимаем на крестик во всплывающем окне Создание справочника
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Создание справочника через кнопку Отменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_creating_catalogue_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Переходим к созданию справочника
        self.APP.web_custom_field_dictionary.button_create_catalogue()
        # Нажимаем на кнопку Отменить во всплывающем окне Создание справочника
        self.APP.web_custom_field_dictionary.button_cancel_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Удаление справочника через крестик')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_deleting_catalogue_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Переходим к удалению справочника
        self.APP.web_custom_field_dictionary.button_delete_in_pop_up_block_in_tree()
        # Нажимаем на крестик во всплывающем окне Удаление справочника
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Удаление справочника через кнопку Отменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_deleting_catalogue_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Переходим к удалению справочника
        self.APP.web_custom_field_dictionary.button_delete_in_pop_up_block_in_tree()
        # Нажимаем на кнопку Отменить во всплывающем окне Удаление справочника
        self.APP.web_custom_field_dictionary.button_cancel_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Редактирование справочника через крестик')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_editing_catalogue_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Переходим к редактированию справочника
        self.APP.web_custom_field_dictionary.button_change_in_pop_up_block_in_tree()
        # Нажимаем на крестик во всплывающем окне Редактирование справочника
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Редактирование справочника через кнопку Отменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_editing_catalogue_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к редактированию справочника
        self.APP.web_custom_field_dictionary.button_change_in_pop_up_block_in_tree()
        # Нажимаем на кнопку Отменить во всплывающем окне Редактирование справочника
        self.APP.web_custom_field_dictionary.button_cancel_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Добавление значения через крестик')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_adding_value_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к добавлению значения
        self.APP.web_custom_field_dictionary.button_to_add_value()
        # Нажимаем на крестик во всплывающем окне Добавление значения
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Добавление значения через кнопку Отменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_adding_value_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к добавлению значения
        self.APP.web_custom_field_dictionary.button_to_add_value()
        # Нажимаем на кнопку Отменить во всплывающем окне Добавление значения
        self.APP.web_custom_field_dictionary.button_cancel_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Удаление значения через крестик')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_deleting_value_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к удалению значения
        self.APP.web_custom_field_dictionary.button_delete_in_pop_up_block_in_catalogue()
        # Нажимаем на крестик во всплывающем окне Удаление значения
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Удаление значения через кнопку Отменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_deleting_value_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к удалению значения
        self.APP.web_custom_field_dictionary.button_delete_in_pop_up_block_in_catalogue()
        # Нажимаем на кнопку Отменить во всплывающем окне Удаление значения
        self.APP.web_custom_field_dictionary.button_cancel_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Значение через крестик')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_value_first(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к редактированию значения
        self.APP.web_custom_field_dictionary.button_change_in_pop_up_block_in_catalogue()
        # Нажимаем на крестик во всплывающем окне Значение
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки

    @allure.title('Закрыть окно Значение через кнопку Отменить')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_close_value_second(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Ищем пользовательский справочник
        name_catalogue = 'Тестовый_справочник_31.31.3131'
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(name_catalogue)
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(name_catalogue)
        # Переходим к редактированию значения
        self.APP.web_custom_field_dictionary.button_change_in_pop_up_block_in_catalogue()
        # Нажимаем на крестик во всплывающем окне Значение
        self.APP.web_custom_field_dictionary.button_cross_in_pop_up_block()
        # TODO добавить проверки