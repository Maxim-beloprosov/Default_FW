from Test.G1.web_tests.g1_web_base import G1WebBase
import allure
import pytest

@allure.epic('G1')
@allure.feature('Web - Request')
@allure.story('Согласующие в заявках')
class TestApprovers(G1WebBase):

    @allure.title('Добавить согласующего после создания заявки инициатором')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_add_approver_after_create_request_as_initiator(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Добавляем согласующего
        correct_approver = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_approver(correct_approver)
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальных согласующих
        actual_approvers = self.APP.g1_web_ticket_base.g1_get_approvers_in_ticket()
        # Проверяем количество согласующих
        assert len(actual_approvers) == 1
        # Проверяем конкретного согласующего
        assert correct_approver in actual_approvers

    @allure.title('Добавить согласующего после создания заявки участником ГО')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_add_approver_after_create_request_as_responsibility_group_member(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search()
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Добавляем согласующего
        correct_approver = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_approver(correct_approver)
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальных согласующих
        actual_approvers = self.APP.g1_web_ticket_base.g1_get_approvers_in_ticket()
        # Проверяем количество согласующих
        assert len(actual_approvers) == 1
        # Проверяем конкретного согласующего
        assert correct_approver in actual_approvers

    @allure.title('Добавить согласующего после создания заявки исполнителем')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Белопросов Максим')
    @pytest.mark.Gandiva1
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_add_approver_after_create_request_as_contractor(self):
        # Создаем заявку
        self.APP.g1_web_request_new.g1_create_request_use_global_search()
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Назначаем заявку на себя
        self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Добавляем согласующего
        correct_approver = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_approver(correct_approver)
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальных согласующих
        actual_approvers = self.APP.g1_web_ticket_base.g1_get_approvers_in_ticket()
        # Проверяем количество согласующих
        assert len(actual_approvers) == 1
        # Проверяем конкретного согласующего
        assert correct_approver in actual_approvers