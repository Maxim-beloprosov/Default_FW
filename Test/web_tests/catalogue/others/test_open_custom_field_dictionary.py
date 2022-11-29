import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Custom Field Dictionary')
@allure.story('Переходы на страницу пользовательских справочников')
class TestOpenCustomFieldDictionary(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    correct_title_on_page_custom_field_dictionary = {
        'correct_title_rus': 'Справочники',
        'correct_title_eng': 'References'
    }

    @allure.title('Переход к пользовательским справочникам через левое боковое меню Master Layout')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_open_custom_field_dictionary_first(self):
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'catalogue/others/'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_custom_field_dictionary['correct_title_rus'] or actual_title == self.correct_title_on_page_custom_field_dictionary['correct_title_eng']

    @allure.title('Переход к пользовательским справочникам через страницу справочников')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_button_to_open_custom_field_dictionary_second(self):
        # Переходим на страницу справочников
        self.APP.web_any_page.click_catalogue_left_menu()
        # Переходим к пользовательским справочникам
        self.APP.web_catalogue.switching_to_custom_field_dictionaries()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'catalogue/others/'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_custom_field_dictionary['correct_title_rus'] or actual_title == self.correct_title_on_page_custom_field_dictionary['correct_title_eng']
