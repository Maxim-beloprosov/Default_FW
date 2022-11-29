import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "Новая"')
class TestChangeStatusTheRequestFromNew(WebBase):

    @allure.title('Смена статуса с "Новая" на "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_new_to_work(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        correct_status = self.APP.group_data.Status_ticket['request_and_task']['RUS']['В работе']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_new_to_agreement(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем согласующего
        self.APP.web_tickets_base.add_approver(self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name'])
        correct_status = self.APP.group_data.Status_ticket['request_and_task']['RUS']['На согласовании']
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_new_to_resolved(self):
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user03'])
        # Переходим к созданию заявки по телефону
        self.APP.web_any_page.click_btn_create_phone_request_left_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 12 Заявка по телефону']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        correct_status = self.APP.group_data.Status_ticket['request_and_task']['RUS']['В проверке']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "В ожидании + дата"')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_new_to_waiting(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Изменяем дату создания
        self.APP.web_request_create.edit_start_date_in_request_when_create(self.APP.time.date_increased_x_days(7), '11')
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        correct_status = self.APP.group_data.Status_ticket['request_and_task']['RUS']['В ожидании']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status[0:10]