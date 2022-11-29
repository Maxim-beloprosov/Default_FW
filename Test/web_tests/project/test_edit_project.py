import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Project')
@allure.story('Изменение проекта')
class TestEditProject(WebBase):
    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Добавить дополнительное описание в проекте')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_add_an_additional_description_in_project(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Добавляем дополнительное описание
        correct_additional_description = "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.add_additional_description(correct_additional_description)
        # Получаем информацию о всех описаниях
        list_descriptions = self.APP.web_tickets_base.get_additional_descriptions_in_ticket()
        # Проверяем добавленное дополнительное описание
        # Счетчик 2, т.к. считаем еще и изначальное описание тикета
        assert len(list_descriptions) == 2
        assert correct_additional_description in list_descriptions

    @allure.title('Изменить дополнительное описание в проекте')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_edit_an_additional_description_in_project(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Добавляем дополнительное описание
        self.APP.api_actions_in_project.add_additional_description(project['id'],
            "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Изменяем дополнительное описание
        correct_additional_description = "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_project_id.edit_additional_description(1, correct_additional_description)
        # Получаем информацию о всех описаниях
        list_descriptions = self.APP.web_tickets_base.get_additional_descriptions_in_ticket()
        # Проверяем добавленное дополнительное описание
        # Счетчик 2, т.к. считаем еще и изначальное описание тикета
        assert len(list_descriptions) == 2
        assert correct_additional_description in list_descriptions

    @allure.title('Отменить проект')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_cancel_a_project(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Отменяем проект
        correct_status = self.APP.web_tickets_base.canceling_of_ticket()
        # Возвращаем статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Перевести проект в проверку')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_project_for_resolve(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Авторизуемся руководителем проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Переводим проект в проверку
        self.APP.web_tickets_base.click_btn_ticket_for_resolve()
        correct_status = 'В проверке'
        # Возвращаем статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Принять согласование в проекте')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_accept_the_agreement_in_project(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver]})
        # Авторизуемся руководителем проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Принимаем согласование
        self.APP.web_tickets_base.accept_the_agreement()
        correct_status = 'В работе'
        # Ожидаем, пока будет корректный статус у проекта в апи, далее получаем актуальный статус проекта с WEB
        self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Возвращаем статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Отклонить согласование в проекте')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_reject_the_agreement_in_project(self):
        # Создаем проект с согласующим
        approver = 'test_user05'
        project = self.create_project({"contractorId": 'test_user01', "approvers": [approver]})
        # Авторизуемся руководителем проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Отклоняем согласование
        correct_status = self.APP.web_tickets_base.reject_the_agreement()
        # Возвращаем статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Вернуть проект в работу')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_return_project_to_work(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Авторизуемся руководителем проекта
        self.APP.api_token.get_token('test_user01')
        # Переводим проект в проверку
        self.APP.api_actions_in_project.send_project_to_resolved(project['syncToken'], project['id'])
        # Авторизуемся руководителем проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Переводим тикет в работу
        correct_status = self.APP.web_tickets_base.comeback_a_ticket_in_work()
        # Возвращаем статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Отправить проект на доработку')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_project_for_overwork(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Авторизуемся руководителем проекта
        self.APP.api_token.get_token('test_user01')
        # Переводим проект в проверку
        self.APP.api_actions_in_project.send_project_to_resolved(project['syncToken'], project['id'])
        # Авторизуемся инициатором проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Отправляем заявку на доработку
        correct_status = self.APP.web_tickets_base.ticket_to_overwork()
        # Сравниваем 2 статуса заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Изменить исполнителя в проекте')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_changing_a_contractor_in_project(self):
        # Создаем проект
        project = self.create_project({"contractorId": 'test_user01'})
        # Авторизуемся инициатором проекта
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(project['ticketType'], project['docNumber'])
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Изменяем исполнителя
        correct_contractor = self.APP.group_data.users['test_user02']['Surname'] + ' ' + self.APP.group_data.users['test_user02']['Name']
        self.APP.web_project_id.changing_contractor(correct_contractor)
        # Возвращаем исполнителя заявки
        actual_contractor = self.APP.web_project_id.get_contractor_ticket()
        # Сравниваем 2ух исполнителей
        assert correct_contractor == actual_contractor
