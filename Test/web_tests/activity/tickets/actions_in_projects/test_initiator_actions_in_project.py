import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Initiator actions in project')
@allure.story('Активности инициатора в проекте')
class TestInitiatorActionsInProject(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Отменить проект из Ленты Активности инициатором')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_cancel_project_from_activity_from_initiator(self):
        # Создаем проект
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся руководителем проекта
        self.APP.api_token.get_token(contractor)
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отменяем тикет
        correct_status = self.APP.web_activity.canceling_of_ticket(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    test_data = [1, 2, 3, 4, 5]
    @allure.title('Закрыть проект из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.parametrize('rating', test_data)
    def test_closed_project_from_activity(self, rating):
        # Создаем проект
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Переводим проект в проверку
        task = self.APP.api_actions_in_project.send_project_to_resolved(project['syncToken'], project['id'])
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [task['ticketType'], task['docNumber']]
        # Закрываем тикет с оценкой в 1-5 баллов
        correct_status = self.APP.web_activity.ticket_to_closed_from_activity(type_and_number_a_ticket, rating)
        # Получаем актуальный статус тикета
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Апеллировать проект из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_appeal_project_from_activity(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Принимаем отрицательное решение
        self.APP.api_actions_in_project.reject_project(project['syncToken'], project['id'])
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Апеллируем тикет
        correct_status = self.APP.web_activity.appeal_a_ticket_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем информацию о всех согласующих
        list_approvers = self.APP.web_tickets_base.get_approvers_in_ticket()
        # Формируем ОР согласующего (Руководителя согласующего, который принял отрицательное решение)
        correct_approver = self.users[approver]['Manager']
        correct_approver = self.users[correct_approver]['Surname'] + ' ' + self.users[correct_approver]['Name']
        # Сравниваем 2 статуса
        assert correct_status == actual_status
        # Сравниваем ожидаемого согласующего с фактическим
        assert correct_approver in list_approvers

    @allure.title('Отправить проект на доработку из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_project_for_overwork_from_activity(self):
        # Создаем проект
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Переводим проект в проверку
        project = self.APP.api_actions_in_project.send_project_to_resolved(project['syncToken'], project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Возвращаем тикет на доработку
        correct_status = self.APP.web_activity.ticket_to_overwork_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status
