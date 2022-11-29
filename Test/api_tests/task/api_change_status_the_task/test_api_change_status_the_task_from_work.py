import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "В работе"')
class TestApiChangeStatusTheTaskFromWork(ApiBase):

    @allure.title('Смена статуса с "В работе" на "На согласовании" при добавлении согласующего инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_work_to_agreement_first(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем согласующего в задачу
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "В работе" на "На согласовании" при добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_work_to_agreement_second(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Добавляем согласующего в задачу
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "В работе" на "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_work_to_resolved(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу на проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В проверке']

    @allure.title('Смена статуса с "В работе" на "Ожидает до" при смене даты инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_work_to_waiting_first(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем дату начала
        task['beginDate'] = self.APP.time.get_date_increased_x_days_json(1)
        # Обновляем задачу (Смена даты начала)
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "В работе" на "На уточнении у иниц." при уточнении исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_work_to_initiator_clarification(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "В работе" на "Ожидает до" при смене даты модератором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_work_to_waiting_second(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на  пользователя с режимом модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем дату начала
        task['beginDate'] = self.APP.time.get_date_increased_x_days_json(1)
        # Обновляем задачу (Смена даты начала)
        task = self.APP.api_tasks.put_tasks_id(task['id'], task, 'isModeratorMode=true')
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']


