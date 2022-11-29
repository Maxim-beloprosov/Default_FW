import time

import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение статуса задачи из статуса "В работе"')
class TestWebChangeStatusTheTaskFromWork(WebBase):

    @allure.title('Смена статуса с "В работе" на "На согласовании" при добавлении согласующего инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_work_to_agreement_first(self):
        # Создаем задачу
        task = self.create_task({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
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

    @allure.title('Смена статуса с "В работе" на "На согласовании" при добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_work_to_agreement_second(self):
        # Создаем задачу
        task = self.create_task({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
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

    @allure.title('Смена статуса с "В работе" на "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_work_to_resolved(self):
        # Создаем задачу
        task = self.create_task({'contractorId': 'test_user02', "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user02'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Отправляем задачу в проверку
        self.APP.web_tickets_base.click_btn_ticket_for_resolve()
        correct_status = 'В проверке'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В работе" на "В ожидании" при смене даты начала инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_web_change_status_in_task_from_work_to_waiting(self):
        # Создаем задачу
        task = self.create_task({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        date = self.APP.time.date_increased_x_days(1)
        # Меняем дату начала
        self.APP.web_tickets_base.edit_start_date_in_task_or_project_after_create(date, '11')
        correct_status = 'В ожидании'
        time.sleep(1)
        # Получаем актуальный статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status[0:10]
