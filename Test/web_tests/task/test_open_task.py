import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Переходы на страницу создания задачи')
class TestOpenTask(WebBase):

    correct_title_on_page_on_create_task = {
        'correct_title_rus': 'Создание задачи',
        'correct_title_eng': 'Task creation'
    }

    @allure.title('Переход к созданию задачи через "+" на главной странице')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_task_first(self):
        self.APP.web_any_page.click_btn_create_task_plus_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/task/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_on_create_task['correct_title_rus'] or actual_title == self.correct_title_on_page_on_create_task['correct_title_eng']

    @allure.title('Переход к созданию задачи через кнопку тикетов на главной странице')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_task_second(self):
        self.APP.web_any_page.click_btn_create_task_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/task/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_on_create_task['correct_title_rus'] or actual_title == self.correct_title_on_page_on_create_task['correct_title_eng']

    @allure.title('Переход к созданию задачи через кнопку на странице списка тикетов')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_task_third(self):
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Переходим к созданию задачи
        self.APP.web_tickets_list.button_to_create_task()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'tickets/task/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_on_create_task['correct_title_rus'] or actual_title == self.correct_title_on_page_on_create_task['correct_title_eng']

