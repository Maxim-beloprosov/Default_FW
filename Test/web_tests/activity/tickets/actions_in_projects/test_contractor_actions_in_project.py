import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Contractor actions in project')
@allure.story('Активности исполнителя в проекте')
class TestContractorActionsInProject(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Перевести проект в проверку из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_project_to_resolve_from_activity(self):
        # Создаем проект
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[contractor])
        # Переводим тикет в проверку
        correct_status = self.APP.web_activity.send_ticket_for_resolve(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Вернуть проект в работу из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_comeback_project_in_work_from_activity(self):
        # Создаем проект
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)
        # Переводим задачу в проверку
        self.APP.api_actions_in_project.send_project_to_resolved(project['syncToken'], project['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[contractor])
        # Возвращаем тикет в работу
        correct_status = self.APP.web_activity.comeback_a_ticket_in_work_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Отменить проект из Ленты Активности руководителем проекта')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')@allure.epic('G2')
    def test_cancel_project_from_activity_from_contractor(self):
        # Создаем проект
        contractor = 'test_user01'
        project = self.create_project({"contractorId": contractor, "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')
        # Пишем комментарий, чтобы тикет отобразился в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся руководителем проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[contractor])
        # Отменяем тикет
        correct_status = self.APP.web_activity.canceling_of_ticket(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

