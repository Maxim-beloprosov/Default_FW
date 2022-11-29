import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение задачи')
class TestEditTask(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Добавить дополнительное описание в задаче')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_add_an_additional_description_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Добавляем дополнительное описание
        correct_additional_description = "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.add_additional_description(correct_additional_description)
        # Получаем информацию о всех описаниях
        list_descriptions = self.APP.web_tickets_base.get_additional_descriptions_in_ticket()
        # Проверяем добавленное дополнительное описание
        # Счетчик 2, т.к. считаем еще и изначальное описание тикета
        assert len(list_descriptions) == 2
        assert correct_additional_description in list_descriptions

    @allure.title('Изменить дополнительное описание в задаче')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_edit_an_additional_description_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем описание к задаче
        self.APP.api_actions_in_task.add_additional_descriptions_in_task(task['id'], {'type': 'Text', 'text': "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Изменяем дополнительное описание
        correct_additional_description = "TestAdditionalDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.edit_additional_description(1, correct_additional_description)
        # Получаем информацию о всех описаниях
        list_descriptions = self.APP.web_tickets_base.get_additional_descriptions_in_ticket()
        # Проверяем добавленное дополнительное описание
        # Счетчик 2, т.к. считаем еще и изначальное описание тикета
        assert len(list_descriptions) == 2
        assert correct_additional_description in list_descriptions

    @allure.title('Отменить задачу')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_cancel_a_task(self):
        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user09'})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Отменяем задачу
        correct_status = self.APP.web_tickets_base.canceling_of_ticket()
        # Возвращаем статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Перевести задачу в проверку')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_task_for_resolve(self):
        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user01'})
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Переводим задачу в проверку
        self.APP.web_tickets_base.click_btn_ticket_for_resolve()
        correct_status = 'В проверке'
        # Возвращаем статус заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса
        assert correct_status == actual_status

    @allure.title('Принять согласование в задаче')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_accept_the_agreement_in_task(self):
        # Создаем задачу
        approver = 'test_user05'
        task = self.create_task({"approvers": [approver]})
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Принимаем согласование
        self.APP.web_tickets_base.accept_the_agreement()
        correct_status = 'В работе'
        # Ожидаем, пока будет корректный статус у задачи в апи, далее получаем актуальный статус задачи с WEB
        self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса задачи
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Отклонить согласование в задаче')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_reject_the_agreement_in_task(self):
        # Создаем задачу
        approver = 'test_user05'
        task = self.create_task({"approvers": [approver]})
        # Авторизуемся согласующим
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users[approver])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Отклоняем согласование
        correct_status = self.APP.web_tickets_base.reject_the_agreement()
        # Сравниваем 2 статуса задачи
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Вернуть задачу в работу')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_return_task_to_work(self):
        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user01'})
        # Авторизуемся исполнителем
        self.APP.api_token.get_token('test_user01')
        # Переводим заявку в проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Переводим тикет в работу
        correct_status = self.APP.web_tickets_base.comeback_a_ticket_in_work()
        # Сравниваем 2 статуса заявки
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Отправить задачу на доработку')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_task_for_overwork(self):
        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user01'})
        # Авторизуемся исполнителем
        self.APP.api_token.get_token('test_user01')
        # Переводим заявку в проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Отправляем заявку на доработку
        correct_status = self.APP.web_task_id.ticket_to_overwork()
        # Сравниваем 2 статуса заявки
        actual_status = self.APP.web_task_id.get_status_ticket()
        assert correct_status == actual_status

    @allure.title('Изменить исполнителя в задаче')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_edit_contractor_in_task(self):
        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user01'})
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Изменяем исполнителя
        correct_contractor = self.APP.web_tickets_base.changing_contractor(self.APP.group_data.users['test_user02']['Surname'] + ' ' + self.APP.group_data.users['test_user02']['Name'])
        # Возвращаем исполнителя заявки
        actual_contractor = self.APP.web_tickets_base.get_contractor_ticket()
        # Сравниваем 2ух исполнителей
        assert correct_contractor == actual_contractor