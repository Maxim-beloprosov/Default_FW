import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Изменение заявки')
class TestEditRequest(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Добавить дополнительное описание в заявке')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.JenkinsTest
    def test_add_an_additional_description_in_request(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Добавляем дополнительное описание
        correct_additional_description = "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.add_additional_description(correct_additional_description)
        # Получаем информацию о всех описаниях
        list_descriptions = self.APP.web_tickets_base.get_additional_descriptions_in_ticket()
        # Проверяем добавленное дополнительное описание
        # Счетчик 2, т.к. считаем еще и изначальное описание тикета
        assert len(list_descriptions) == 2
        assert correct_additional_description in list_descriptions

    @allure.title('Изменить дополнительное описание в заявке')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.JenkinsTest
    def test_edit_an_additional_description_in_request(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Добавляем дополнительное описание к заявке
        self.APP.api_actions_in_request.add_additional_descriptions_in_request(request['id'], {'type': 'Text', 'text': "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Изменяем дополнительное описание
        correct_additional_description = "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.edit_additional_description(1, correct_additional_description)
        # Получаем информацию о всех описаниях
        list_descriptions = self.APP.web_tickets_base.get_additional_descriptions_in_ticket()
        # Проверяем добавленное дополнительное описание
        # Счетчик 2, т.к. считаем еще и изначальное описание тикета
        assert len(list_descriptions) == 2
        assert correct_additional_description in list_descriptions

    @allure.title('Назначить заявку на себя')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.JenkinsTest
    def test_assign_request_to_me(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Назначаем заявку на себя
        correct_contractor = self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name']
        self.APP.web_request_id.assign_request_to_me()
        # Возвращаем исполнителя заявки
        actual_contractor = self.APP.web_tickets_base.get_contractor_ticket()
        # Сравниваем 2ух исполнителей
        assert correct_contractor == actual_contractor

    @allure.title('Вернуть заявку в работу')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.JenkinsTest
    def test_return_request_to_work(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Переводим заявку в проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Возвращаем тикет в работу
        correct_status = self.APP.web_tickets_base.comeback_a_ticket_in_work()
        # Сравниваем 2 статуса заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Отправить заявку на доработку')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.JenkinsTest
    def test_send_request_for_overwork(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Переводим заявку в проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Возвращаем заявку на доработку
        correct_status = self.APP.web_tickets_base.ticket_to_overwork()
        # Сравниваем 2 статуса заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Изменить исполнителя в заявке')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.JenkinsTest
    def test_changing_a_contractor_in_request(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Изменяем исполнителя
        correct_contractor = self.APP.group_data.users['test_user02']['Surname'] + ' ' + self.APP.group_data.users['test_user02']['Name']
        self.APP.web_tickets_base.changing_contractor(correct_contractor)
        # Возвращаем исполнителя заявки
        actual_contractor = self.APP.web_tickets_base.get_contractor_ticket()
        # Сравниваем 2ух исполнителей
        assert correct_contractor == actual_contractor