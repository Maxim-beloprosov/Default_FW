import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение статуса задачи из статуса "На согласовании"')
class TestWebChangeStatusTheTaskFromAgreement(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user05')

    @allure.title('Смена статуса с "На согласовании" на "В работе" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_agreement_to_work(self):
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user09'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Принимаем согласование
        self.APP.web_tickets_base.accept_the_agreement()
        correct_status = 'В работе'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "Ожидает до" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_agreement_to_waiting(self):
        # Создаем задачу  согласующим и датой начала
        task = self.create_task(
            {'approvers': ['test_user09'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], 'beginDate': 1})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Принимаем согласование
        self.APP.web_tickets_base.accept_the_agreement()
        correct_status = 'В ожидании'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status[0:10]

    @allure.title('Смена статуса с "На согласовании" на "Отклонена" при отрицательном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_agreement_to_reject(self):
        # Создаем задачу
        task = self.create_task(
            {'approvers': ['test_user09'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Отклоняем согласование
        self.APP.web_tickets_base.reject_the_agreement()
        correct_status = 'Отклонена'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у иниц."')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip(reason=' Проблемы с CK Editor')
    def test_change_status_in_task_from_agreement_to_initiator_clarification(self):
        # Создаем задачу
        task = self.create_task(
            {'approvers': ['test_user09'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Задаем вопрос-уточнение
        self.APP.web_tickets_base.ask_initiator_clarification('AutomationWebTest clarification')
        correct_status = 'На уточнении у иниц.'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у исп."')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @pytest.mark.skip(reason=' Проблемы с CK Editor')
    def test_change_status_in_task_from_agreement_to_contractor_clarification(self):
        # Создаем задачу
        task = self.create_task(
            {'approvers': ['test_user09'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Задаем вопрос-уточнение
        self.APP.web_tickets_base.ask_contractor_clarification('AutomationWebTest clarification')
        correct_status = 'На уточнении у исп.'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status

