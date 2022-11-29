import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Approver actions in project')
@allure.story('Активности согласующего в проекте')
class TestApproverActionsInTask(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Отклонить проект в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_reject_project_from_activity(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Принимаем отрицательное решение
        correct_status = self.APP.web_activity.reject_the_agreement_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Согласовать проект в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_accept_project_from_activity(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Принимаем положительное решение
        correct_status = 'В работе'
        self.APP.web_activity.accept_the_agreement_from_activity(type_and_number_a_ticket[1])
        # Ожидаем, пока будет корректный статус у тикета в апи
        self.APP.web_tickets_base.waiting_the_correct_status(self.APP.group_data.Status_ticket['ENG'][correct_status],
                                                             type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Делегировать согласование в проекте в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_delegate_agreement_in_project_from_activity(self):
        # Создаем проект с согласующим
        approver = 'test_Boss03'
        delegate_approver = self.APP.group_data.users[approver]['Surname'] + ' ' + self.APP.group_data.users[approver]['Name']
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Делегируем согласование
        correct_approver = self.APP.group_data.users['test_Boss02']['Surname'] + ' ' + self.APP.group_data.users['test_Boss02']['Name']
        self.APP.web_activity.delegate_the_agreement_from_activity(type_and_number_a_ticket[1], correct_approver)
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем информацию о всех согласующих
        list_approvers = self.APP.web_tickets_base.get_approvers_in_ticket()
        # Проверяем добавленного согласующего
        assert len(list_approvers) == 2
        assert correct_approver in list_approvers
        assert delegate_approver in list_approvers

    @allure.title('Задать уточнение инициатору в проекте из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_ask_initiator_clarification_in_project_from_activity(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Задаем уточнение инициатору
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у иниц.']
        self.APP.web_activity.ask_initiator_clarification_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Задать уточнение исполнителю в проекте из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_ask_contractor_clarification_in_project_from_activity(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Задаем уточнение исполнителю
        correct_status = self.status_ticket['request_and_task']['RUS']['На уточнении у исп.']
        self.APP.web_activity.ask_contractor_clarification_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status