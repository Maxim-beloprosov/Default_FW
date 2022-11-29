import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Project')
@allure.story('Переходы на страницу создания проекта')
class TestOpenCreateProject(WebBase):

    correct_title_on_page_create_project = {
        'correct_title_rus': 'Создание проекта',
        'correct_title_eng': 'Project Creation'
    }

    @allure.title('Переход к созданию проекта через "+" на главной странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_project_first(self):
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'projects/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_create_project['correct_title_rus'] or actual_title == self.correct_title_on_page_create_project['correct_title_eng']

    @allure.title('Переход к созданию проекта через кнопку проектов на главной странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_project_second(self):
        self.APP.web_any_page.click_btn_create_project_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'projects/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_create_project['correct_title_rus'] or actual_title == self.correct_title_on_page_create_project['correct_title_eng']

    @allure.title('Переход к созданию проекта через кнопку на странице списка проектов')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_create_project_third(self):
        # Переходим в список проектов
        self.APP.web_any_page.click_project_left_menu()
        # Переходим к созданию проекта
        self.APP.web_project_list.button_to_create_project()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'projects/create'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_create_project['correct_title_rus'] or actual_title == self.correct_title_on_page_create_project['correct_title_eng']





