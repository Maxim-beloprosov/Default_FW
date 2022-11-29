import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Custom Field Dictionary')
@allure.story('Создание пользовательского справочника')
class TestCreateCustomFieldDictionary(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_api_user'])

    @allure.title('Создание справочника с текстовым полем')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_custom_field_dictionary_with_text_field(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Нажимаем на кнопку "Создать справочник"
        self.APP.web_custom_field_dictionary.button_create_catalogue()
        # Заполняем название справочника
        correct_name_catalogue = 'TestOthersCatalogue AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_custom_field_dictionary.fill_name_catalogue(correct_name_catalogue)
        # Заполняем название поля
        self.APP.web_custom_field_dictionary.fill_name_field("TestFiled AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Нажимаем кнопку Создать
        self.APP.web_custom_field_dictionary.button_create_in_pop_up_block()
        # Ищем пользовательский справочник
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(correct_name_catalogue[-8:])
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(correct_name_catalogue)
        # Получаем название выбранного справочника
        actual_name_catalogue = self.APP.web_custom_field_dictionary.get_name_custom_field_dictionary()
        # Переходим в редактирование пользовательского справочника
        self.APP.web_custom_field_dictionary.button_change_in_pop_up_block_in_tree()
        # Проверяем статус пользовательского справочника (Используется/Не используется)
        status = self.APP.web_custom_field_dictionary.check_status_custom_field_dictionary('use')
        # Сравниваем названия справочника с ОР
        assert correct_name_catalogue == actual_name_catalogue
        # Проверяем статус пользовательского справочника (Если False, статус справочника неверный)
        assert status

    @allure.title('Создание не используемого справочника с текстовым полем')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_not_used_custom_field_dictionary_with_text_field(self):
        # Переходим на страницу пользовательских справочников
        self.APP.web_any_page.click_others_catalogue_left_menu()
        # Нажимаем на кнопку "Создать справочник"
        self.APP.web_custom_field_dictionary.button_create_catalogue()
        # Заполняем название справочника
        correct_name_catalogue = 'TestOthersCatalogue AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_custom_field_dictionary.fill_name_catalogue(correct_name_catalogue)
        # Активируем статус Не используется
        self.APP.web_custom_field_dictionary.click_status_for_not_used()
        # Заполняем название поля
        self.APP.web_custom_field_dictionary.fill_name_field("TestFiled AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Нажимаем кнопку Создать
        self.APP.web_custom_field_dictionary.button_create_in_pop_up_block()
        # Ищем пользовательский справочник
        self.APP.web_custom_field_dictionary.fill_text_for_search_in_tree(correct_name_catalogue[-8:])
        # Выбираем нужный справочник
        self.APP.web_custom_field_dictionary.go_to_catalogue_in_list(correct_name_catalogue)
        # Получаем название выбранного справочника
        actual_name_catalogue = self.APP.web_custom_field_dictionary.get_name_custom_field_dictionary()
        # Переходим в редактирование пользовательского справочника
        self.APP.web_custom_field_dictionary.button_change_in_pop_up_block_in_tree()
        # Проверяем статус пользовательского справочника (Используется/Не используется)
        status = self.APP.web_custom_field_dictionary.check_status_custom_field_dictionary('not_use')
        # Сравниваем названия справочника с ОР
        assert correct_name_catalogue == actual_name_catalogue
        # Проверяем статус пользовательского справочника (Если False, статус справочника неверный)
        assert status
