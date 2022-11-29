import time

import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Activity')
@allure.story('Переход в в тикеты из Ленты Активности')
class TestOpenTicketsFromActivity(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Переход в заявку из Ленты Активности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_open_request_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        correct_info_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(correct_info_ticket[1])
        # Получаем тип и номера тикета
        actual_info_ticket = self.APP.web_tickets_base.get_type_and_number_ticket()
        # Сравниваем информацию тикета ФР и ОР
        assert correct_info_ticket[1] == actual_info_ticket[1]
        # Перевожу в нижний регистр тип тикета (Request = request)
        assert (correct_info_ticket[0]).lower() == (actual_info_ticket[0]).lower()

    @allure.title('Переход в задачу из Ленты Активности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_open_task_from_activity(self):
        # Создаем задачу
        contractor = 'test_user01'
        task = self.create_task({"contractorId": contractor})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Выносим тип и номер тикета
        correct_info_ticket = [task['ticketType'], task['docNumber']]
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[contractor])
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(correct_info_ticket[1])
        # Получаем тип и номера тикета
        actual_info_ticket = self.APP.web_tickets_base.get_type_and_number_ticket()
        # Сравниваем информацию тикета ФР и ОР
        assert correct_info_ticket[1] == actual_info_ticket[1]
        # Перевожу в нижний регистр тип тикета (Task = task)
        assert (correct_info_ticket[0]).lower() == (actual_info_ticket[0]).lower()

    @allure.title('Переход в проект из Ленты Активности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_open_project_from_activity(self):
        # Создаем проект
        manager = 'test_user01'
        project = self.create_project({"contractorId": manager})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(project['id'])
        # Выносим тип и номер тикета
        correct_info_ticket = [project['ticketType'], project['docNumber']]
        # Авторизуемся руководителем проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[manager])
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(correct_info_ticket[1])
        # Получаем тип и номера тикета
        actual_info_ticket = self.APP.web_tickets_base.get_type_and_number_ticket()
        # Сравниваем информацию тикета ФР и ОР
        assert correct_info_ticket[1] == actual_info_ticket[1]
        # Перевожу в нижний регистр тип тикета (Project = project)
        assert (correct_info_ticket[0]).lower() + 's' == (actual_info_ticket[0]).lower()
