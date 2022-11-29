import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Messenger')
@allure.story('Переходы на страницу чатов')
class TestOpenMessenger(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    correct_title_on_page_messenger = {
        'correct_title_rus': 'Чаты',
        'correct_title_eng': 'Chats'
    }

    @allure.title('Переход к чатам через левое боковое меню Master Layout')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_open_messenger_left_menu(self):
        self.APP.web_any_page.click_messenger_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'messenger/'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_messenger.get_text_title_on_the_page_messenger()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_messenger['correct_title_rus'] or actual_title == self.correct_title_on_page_messenger['correct_title_eng']
