import allure
import pytest

from Test.G1.web_tests.g1_web_base import G1WebBase


@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "В работе"')
class TestChangeStatusTheRequestFromWork(G1WebBase):

    @allure.title('Смена статуса с "В работе" на "Отменено", когда исполнитель не назначен')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_work_to_cancel(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Отменяем заявку
        correct_status = self.APP.g1_web_ticket_base.g1_canceling_of_ticket()
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В работе" на "В проверке"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_work_to_resolved(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Назначаем заявку на себя
        self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Переводим заявку в работу
        correct_status = self.APP.g1_web_ticket_base.g1_send_ticket_for_resolve()
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В работе" на "На согласовании"')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_work_to_agreement(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Добавляем согласующего
        self.APP.g1_web_ticket_base.g1_add_approver('user5 test')
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На согласовании']
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В работе" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_work_to_initiator_clarification_first(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Задаем уточнение инициатору
        self.APP.g1_web_ticket_base.g1_ask_initiator_clarification()
        correct_status = self.APP.group_data.g1_Status_ticket['WEB']['На уточнении у инициатора']
        # Получаем актуальный статус заявки
        actual_status = self.APP.g1_web_ticket_base.g1_get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Смена статуса с "В работе" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    def test_change_status_in_request_from_work_to_initiator_clarification_second(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
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