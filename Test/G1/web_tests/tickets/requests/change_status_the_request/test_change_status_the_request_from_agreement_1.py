import allure
import pytest

from Test.G1.web_tests.g1_web_base import G1WebBase


@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "На согласовании"')
class TestChangeStatusTheRequestFromAgreement(G1WebBase):

    @allure.title('Смена статуса с "На согласовании" на "В работе", когда согласующий принимает положительное решение')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_work(self):
        approver = 'user5 test'
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver=approver)
        # Авторизуемся согласующим
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need(approver)
        # Принимаем положительное решение
        self.APP.g1_web_ticket_base.g1_accept_the_agreement()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['В работе']
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "Отменено", когда исполнитель не назначен')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_cancel(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver='user5 test')
        # Отменяем заявку
        correct_status = self.APP.g1_web_ticket_base.g1_canceling_of_ticket()
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "Ожидает"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_waiting(self):
        approver = 'user5 test'
        correct_date_start = self.APP.time.date_increased_x_days(2)
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver='user5 test', date_start=correct_date_start)
        # Авторизуемся согласующим
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need(approver)
        # Принимаем положительное решение
        self.APP.g1_web_ticket_base.g1_accept_the_agreement()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['Ожидает'] + ' ' + correct_date_start
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "Отклонено"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_rejected(self):
        approver = 'user5 test'
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver=approver)
        # Авторизуемся согласующим
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need(approver)
        # Принимаем отрицательное решение
        correct_status = self.APP.g1_web_ticket_base.g1_reject_the_agreement()
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_initiator_clarification_first(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver='user5 test')
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Задаем уточнение инициатору
        self.APP.g1_web_ticket_base.g1_ask_initiator_clarification()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На уточнении у инициатора']
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_initiator_clarification_second(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver='user5 test')
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Назначаем заявку на себя
        self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Задаем уточнение инициатору
        self.APP.g1_web_ticket_base.g1_ask_initiator_clarification()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На уточнении у инициатора']
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает согласующий не принявший решение')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_initiator_clarification_third(self):
        approver = 'user5 test'
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver=approver)
        # Авторизуемся согласующим
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need(approver)
        # Задаем уточнение инициатору
        self.APP.g1_web_ticket_base.g1_ask_initiator_clarification()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На уточнении у инициатора']
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Исполнителя", когда уточнение задает согласующий не принявший решение')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_agreement_to_contractor_clarification(self):
        approver = 'user5 test'
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search(approver=approver)
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Назначаем заявку на себя
        self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Авторизуемся согласующим
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need(approver)
        # Задаем уточнение исполнителю
        self.APP.g1_web_ticket_base.g1_ask_contractor_clarification()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На уточнении у исполнителя']
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status
