import allure
import pytest

from Test.G1.web_tests.g1_web_base import G1WebBase


@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "Новая"')
class TestChangeStatusTheRequestFromNew(G1WebBase):

    @allure.title('Смена статуса с "Новая" на "В работе"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_new_to_work_test(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['В работе']
        # Возвращаем статус тикета
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "Ожидает"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_new_to_waiting_test(self):
        correct_date_start = self.APP.time.date_increased_x_days(2)
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(date_start=correct_date_start)
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['Ожидает'] + ' ' + correct_date_start
        # Возвращаем статус тикета
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "На согласовании"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_new_to_agreement_test(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver='user5 test')
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На согласовании']
        # Возвращаем статус тикета
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status