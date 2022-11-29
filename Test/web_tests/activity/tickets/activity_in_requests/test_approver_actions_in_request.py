import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Approver actions in request')
@allure.story('Активности согласующего в заявке')
class TestApproverActionsInRequest(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Отклонить заявку в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_reject_request_from_activity(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Принимаем отрицательное решение
        correct_status = self.APP.web_activity.reject_the_agreement_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Согласовать заявку в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_accept_request_from_activity(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        comment = self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Принимаем положительное решение
        correct_status = 'В работе'
        self.APP.web_activity.accept_the_agreement_from_activity(type_and_number_a_ticket[1])
        # Ожидаем, пока будет корректный статус у заявки в апи
        self.APP.web_tickets_base.waiting_the_correct_status(self.APP.group_data.Status_ticket['ENG'][correct_status],
                                                             type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Делегировать согласование в заявке в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_delegate_agreement_in_request_from_activity(self):
        # Создаем заявку с согласующим
        approver = 'test_Boss03'
        delegate_approver = self.APP.group_data.users[approver]['Surname'] + ' ' + self.APP.group_data.users[approver]['Name']
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Делегируем согласование
        correct_approver = self.APP.group_data.users['test_Boss02']['Surname'] + ' ' + self.APP.group_data.users['test_Boss02']['Name']
        self.APP.web_activity.delegate_the_agreement_from_activity(type_and_number_a_ticket[1], correct_approver)
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Получаем информацию о всех согласующих
        list_approvers = self.APP.web_tickets_base.get_approvers_in_ticket()
        # Проверяем добавленного согласующего
        assert len(list_approvers) == 2
        assert correct_approver in list_approvers
        assert delegate_approver in list_approvers

    @allure.title('Задать уточнение инициатору в заявке из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_ask_initiator_clarification_in_request_from_activity(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Задаем уточнение инициатору
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        self.APP.web_activity.ask_initiator_clarification_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Задать уточнение исполнителю в заявке из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_ask_contractor_clarification_in_request_from_activity(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Задаем уточнение исполнителю
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у исп.']
        self.APP.web_activity.ask_contractor_clarification_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status