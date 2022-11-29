import time

import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение статуса задачи из статуса "В проверке"')
class TestWebChangeStatusTheTaskFromWork(WebBase):

    @allure.title('Смена статуса с "В проверке" на "В работе" при отправке на доработку инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_resolved_to_work(self):
        # Создаем задачу
        task = self.create_task({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Перелогиниваемся под исполнителем
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу на проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Отправляем задачу на доработку
        self.APP.web_tickets_base.ticket_to_overwork()
        correct_status = 'В работе'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    test_data = [1, 2, 3, 4, 5]

    @allure.title('Смена статуса задачи с "В проверке" на "Закрыта"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.parametrize('rating', test_data)
    def test_web_change_status_in_task_from_resolved_to_closed(self, rating):
        self.APP.api_token.get_token('test_user09')
        # Создаем задачу
        task = self.create_task({'contractorId': 'test_user02', "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Перелогиниваемся под исполнителем
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу на проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Закрываем задачу
        self.APP.web_tickets_base.ticket_to_closed(rating)
        correct_status = 'Закрыта'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

