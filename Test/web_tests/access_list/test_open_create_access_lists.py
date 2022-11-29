import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Access Lists')
@allure.story('Переходы на страницу создания листов допусков')
class TestOpenCreateAccessLists(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    correct_title_on_page_create_access_list = {
        'correct_title_rus': 'Создание листа допуска',
        'correct_title_eng': 'Creating an access list'
    }
    @allure.title('Переход к созданию листа допуска через "+" на главной странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_access_lists_first(self):
        self.APP.web_any_page.click_btn_create_access_lists_plus_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'access-lists/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_create_access_list['correct_title_rus'] or actual_title == self.correct_title_on_page_create_access_list['correct_title_eng']

    @allure.title('Переход к созданию листа допуска через левое боковое меню Master Layout')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_access_lists_second(self):
        self.APP.web_any_page.click_btn_create_access_list_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'access-lists/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_create_access_list['correct_title_rus'] or actual_title == self.correct_title_on_page_create_access_list['correct_title_eng']

    @allure.title('Переход к созданию листа допуска через страницу листов допусков')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_access_lists_third(self):
        # Переходим на страницу листов допусков
        self.APP.web_any_page.click_access_lists_left_menu()
        # Нажимаем кнопку Создать лист допуска
        self.APP.web_access_lists.button_to_create_access_list()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'access-lists/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_create_access_list['correct_title_rus'] or actual_title == self.correct_title_on_page_create_access_list['correct_title_eng']

