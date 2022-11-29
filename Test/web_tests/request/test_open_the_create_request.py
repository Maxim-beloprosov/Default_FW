import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Переходы на страницу создания заявки')
class TestOpenCreateRequest(WebBase):

    correct_title_on_page_for_normal_request = {
        'correct_title_rus': 'Создание заявки',
        'correct_title_eng': ''
    }
    correct_title_on_page_for_phone_request = {
        'correct_title_rus': 'Создание заявки по телефону',
        'correct_title_eng': ''
    }

    @allure.title('Переход к созданию заявки через "+" на главной странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_request_first(self):
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/request/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_for_normal_request['correct_title_rus'] or actual_title == self.correct_title_on_page_for_normal_request['correct_title_eng']

    @allure.title('Переход к созданию заявки через кнопку тикетов на главной странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_request_second(self):
        self.APP.web_any_page.click_btn_create_request_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/request/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_for_normal_request['correct_title_rus'] or actual_title == self.correct_title_on_page_for_normal_request['correct_title_eng']

    @allure.title('Переход к созданию заявки через кнопку на странице списка тикетов')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_request_third(self):
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Переходим к созданию заявки
        self.APP.web_tickets_list.button_to_create_request()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/request/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_for_normal_request['correct_title_rus'] or actual_title == self.correct_title_on_page_for_normal_request['correct_title_eng']

    @allure.title('Переход к созданию заявки по телефону через кнопку тикетов на главной странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_phone_request_frist(self):
        self.APP.web_any_page.click_btn_create_phone_request_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/request/create?type=phone'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_for_phone_request['correct_title_rus'] or actual_title == self.correct_title_on_page_for_phone_request['correct_title_eng']

    @allure.title('Переход к созданию заявки по телефону через кнопку на странице списка тикетов')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_phone_request_second(self):
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Переходим к созданию заявки по телефону
        self.APP.web_tickets_list.button_to_create_phone_request()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/request/create?type=phone'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_for_phone_request['correct_title_rus'] or actual_title == self.correct_title_on_page_for_phone_request['correct_title_eng']
