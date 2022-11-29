import time

import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение статуса задачи из статуса "В ожидании"')
class TestWebChangeStatusTheTaskFromWaiting(WebBase):

    @allure.title('Смена статуса с "В ожидании" на "На согласовании" при добавлении согласующего инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_waiting_to_agreement_first(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Добавляем согласующего
        self.APP.web_tickets_base.add_approver('UserOne Test')
        correct_status = 'На согласовании'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании" на "На согласовании" при добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_waiting_to_agreement_second(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user02'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Добавляем согласующего
        self.APP.web_tickets_base.add_approver('UserOne Test')
        correct_status = 'На согласовании'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В ожидании" на "В работе при смене даты начала инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_waiting_to_work(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        date_and_time = self.APP.time.get_time_now().split()
        # Меняем дату начала
        self.APP.web_tickets_base.edit_start_date_in_task_or_project_after_create(date_and_time[0], date_and_time[1][:2])
        correct_status = 'В работе'
        time.sleep(1)
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

