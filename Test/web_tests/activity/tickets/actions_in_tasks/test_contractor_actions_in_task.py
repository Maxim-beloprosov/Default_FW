import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Contractor actions in task')
@allure.story('Активности исполнителя в задаче')
class TestContractorActionsInTask(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Перевести задачу в проверку из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_task_to_resolve_from_activity(self):
        # Создаем задачу
        contractor = 'test_user01'
        task = self.create_task({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [task['ticketType'], task['docNumber']]
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[contractor])
        # Переводим тикет в проверку
        correct_status = self.APP.web_activity.send_ticket_for_resolve(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Вернуть задачу в работу из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_comeback_task_in_work_from_activity(self):
        # Создаем задачу
        contractor = 'test_user01'
        task = self.create_task({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [task['ticketType'], task['docNumber']]
        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)
        # Переводим задачу в проверку
        self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[contractor])
        # Возвращаем тикет в работу
        correct_status = self.APP.web_activity.comeback_a_ticket_in_work_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Отменить задачу из Ленты Активности, когда исполнитель равен инициатору')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_cancel_task_when_initiator_and_contractor_one_user_from_activity(self):
        # Создаем задачу с обозревателем (чтобы от него написать комментарий в тикете, и он появился в Ленте Активности)
        initiator = 'test_user09'
        observer = 'test_user01'
        task = self.create_task({"observers": [observer], "contractorId": initiator, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся обозревателем
        self.APP.api_token.get_token(observer)
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [task['ticketType'], task['docNumber']]
        # Авторизуемся инициатором/исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[initiator])
        # Отменяем тикет
        correct_status = self.APP.web_activity.canceling_of_ticket(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

