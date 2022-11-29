import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "На уточнении у исп."')
class TestChangeStatusTheRequestFromContractorClarification(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "В работе", когда исполнитель ответил на уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_contractor_clarification_to_work_first(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        # Создаем заявку
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Задаем уточнение согласующим исполнителю
        clarification = "TestClarificationForContractor AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'], clarification)
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Отвечаем на уточнение
        self.APP.web_tickets_base.answering_to_comment(clarification)
        correct_status = self.status_ticket['request_and_task']['RUS']['В работе']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "В работе", когда согласующий принял положительное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_contractor_clarification_to_work_second(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        # Создаем заявку
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Задаем уточнение согласующим исполнителю
        clarification = "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'], clarification)
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

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "В ожидании", когда исполнитель ответил на уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_contractor_clarification_to_waiting(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        # Создаем заявку
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "beginDate": 7})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Задаем уточнение согласующим исполнителю
        clarification = "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'], clarification)
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Отвечаем на уточнение
        self.APP.web_tickets_base.answering_to_comment(clarification)
        correct_status = self.status_ticket['request_and_task']['RUS']['В ожидании']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status[0:10]

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "На согласовании", когда исполнитель ответил на уточнение при активном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_contractor_clarification_to_agreement(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        # Создаем заявку
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Задаем уточнение согласующим исполнителю
        clarification = "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'], clarification)
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Отвечаем на уточнение
        self.APP.web_tickets_base.answering_to_comment(clarification)
        correct_status = self.status_ticket['request_and_task']['RUS']['На согласовании']
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "Отклонено", когда согласующий принял отрицательное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_contractor_clarification_to_rejected(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        # Создаем заявку
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Задаем уточнение согласующим исполнителю
        clarification = "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'], clarification)
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

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "Отменено", когда исполнитель не назначен')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_contractor_clarification_to_cancel(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        # Создаем заявку
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Задаем уточнение согласующим исполнителю
        clarification = "TestClarification AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'], clarification)
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