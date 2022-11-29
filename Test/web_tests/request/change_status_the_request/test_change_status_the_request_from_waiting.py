import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "В ожидании"')
class TestChangeStatusTheRequestFromWaiting(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Смена статуса с "В ожидании + дата" на "В работе", когда инициатор удаляет дату начала в разрешенное время')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_waiting_to_work_first(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Удаляем дату начала
        self.APP.web_request_id.delete_start_date_in_request_after_create()
        correct_status = self.status_ticket['request_and_task']['RUS']['В работе']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании + дата" на "В работе", когда исполнитель переводит заявку в работу')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_waiting_to_work_second(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Берем заявку в работу
        correct_status = self.APP.web_tickets_base.take_a_ticket_in_work()
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании + дата" на "Отменено", при отмене инициатором, если исполнитель не назначен')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_waiting_to_cancel(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Отменяем заявку
        correct_status = self.APP.web_tickets_base.canceling_of_ticket()
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании + дата" на "На согласовании", при добавлении согласующего')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_waiting_to_agreement(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Добавляем согласующего
        self.APP.web_tickets_base.add_approver(self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name'])
        correct_status = self.status_ticket['request_and_task']['RUS']['На согласовании']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании + дата" на "На уточнении у инициатора", когда уточнение задает исполнитель')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_waiting_to_initiator_clarification_first(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Задаем уточнение инициатору
        self.APP.web_tickets_base.ask_initiator_clarification(
            "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании + дата" на "На уточнении у инициатора", когда уточнение задает участник ГО')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_waiting_to_initiator_clarification_second(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Задаем уточнение инициатору
        self.APP.web_tickets_base.ask_initiator_clarification(
            "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status