import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "На согласовании"')
class TestChangeStatusTheRequestFromAgreement(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Смена статуса с "На согласовании" на "В работе", когда согласующий принимает положительное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_work(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Принимаем согласование
        self.APP.web_tickets_base.accept_the_agreement()
        correct_status = self.status_ticket['request_and_task']['RUS']['В работе']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "Отменено", когда исполнитель не назначен')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_cancel(self):
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user05'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Отменяем заявку
        correct_status = self.APP.web_tickets_base.canceling_of_ticket()
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "В ожидании + дата"')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_waiting(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Принимаем согласование
        self.APP.web_tickets_base.accept_the_agreement()
        correct_status = self.status_ticket['request_and_task']['RUS']['В ожидании']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status[0:10]

    @allure.title('Смена статуса с "На согласовании" на "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_rejected(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Отклоняем согласование
        correct_status = self.APP.web_tickets_base.reject_the_agreement()
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_initiator_clarification_first(self):
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user05'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Задаем уточнение инициатору
        self.APP.web_tickets_base.ask_initiator_clarification()
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_initiator_clarification_second(self):
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user05'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Задаем уточнение инициатору
        self.APP.web_tickets_base.ask_initiator_clarification()
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает согласующий не принявший решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_initiator_clarification_third(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Задаем уточнение инициатору
        self.APP.web_tickets_base.ask_initiator_clarification(
            "Test Clarification " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Исполнителя", когда уточнение задает согласующий не принявший решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_agreement_to_contractor_clarification(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 11})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Задаем уточнение исполнителю
        self.APP.web_tickets_base.ask_contractor_clarification(
            "Test Clarification " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у исп.']
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status