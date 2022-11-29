import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Contractor actions in request')
@allure.story('Активности исполнителя в заявке')
class TestContractorActionsInRequest(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Перевести заявку в проверку из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_request_to_resolve_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переводим заявку в проверку
        correct_status = self.APP.web_activity.send_ticket_for_resolve(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Вернуть заявку в работу из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_comeback_request_in_work_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Переводим заявку в проверку
        self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Возвращаем заявку в работу
        correct_status = self.APP.web_activity.comeback_a_ticket_in_work_from_activity(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Назначить заявку на себя участником ГО из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_assign_request_to_me_member_go_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся другим участником ГО
        self.APP.api_token.get_token('test_user09')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Назначаем заявку на себя
        correct_contractor = self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name']
        self.APP.web_activity.assign_request_to_me_from_activity(type_and_number_a_ticket, correct_contractor)
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Получаем исполнителя заявки
        actual_contractor = self.APP.web_tickets_base.get_contractor_ticket()
        # Сравниваем 2 статуса
        assert correct_contractor == actual_contractor

    @allure.title('Отменить заявку из Ленты Активности, когда исполнитель равен инициатору')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_cancel_request_from_activity_when_initiator_and_contractor_one_user_from_activity(self):
        # Авторизуемся участником ГО
        initiator = 'test_user01'
        self.APP.api_token.get_token(initiator)
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user04')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[initiator])
        # Отменяем заявку
        correct_status = self.APP.web_activity.canceling_of_ticket(type_and_number_a_ticket)
        # Получаем актуальный статус тикета из Ленты Активности
        actual_status = self.APP.web_activity.get_status_ticket_from_activity(type_and_number_a_ticket[1])
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Эскалировать заявку из Ленты Активности участником ГО')
    @pytest.mark.skip(reason='Не актуальная информация в чек листе, жду исправлений')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_escalate_request_from_activity_firts(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()], "serviceId": self.APP.group_data.service_template['AutomationService Тестовый Тип 20']['name']})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Эскалируем заявку
        self.APP.web_activity.escalate_request_from_activity(type_and_number_a_ticket)
        correct_responsibility_groups = self.APP.group_data.service_template['AutomationService Тестовый Тип 20']['serviceResponsibilityGroups'][1]['responsibilityGroupId']
        # Переходим в тикет с нужным номером
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Получаем актуальную групппа ответственности из заявки
        actual_responsibility_groups = self.APP.web_tickets_base.get_actual_responsibility_groups_in_request()
        # Сравниваем 2 статуса
        assert correct_responsibility_groups == actual_responsibility_groups