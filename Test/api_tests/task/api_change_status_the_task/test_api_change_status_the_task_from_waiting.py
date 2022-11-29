import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "Ожидает до"')
class TestApiChangeStatusTheTaskFromWaiting(ApiBase):

    @allure.title('Смена статуса с "Ожидает до" на "На согласовании" при добавлении согласующего инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_waiting_to_agreement_first(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Добавляем согласующего в задачу
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user01']['user_id'], task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "Ожидает до" на "На согласовании" при добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_waiting_to_agreement_second(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Добавляем согласующего в задачу
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'], task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "Ожидает до" на "В работе" при смене даты начала инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_waiting_to_work_first(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Меняем дату начала в словаре
        task['beginDate'] = '2022-07-20T10:01:43Z'
        # Удаляем дату начала
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "Ожидает до" на "В работе" при смене даты начала модератором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_waiting_to_work_second(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем дату начала в словаре
        task['beginDate'] = '2022-07-20T10:01:43Z'
        # Удаляем дату начала
        task = self.APP.api_tasks.put_tasks_id(task['id'], task, 'isModeratorMode=true')
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "Ожидает до" на "На уточнении у иниц."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_waiting_to_initiator_clarification(self):
        # Создаем задачу с согласующим и датой начала
        task = self.create_task({"approvers": ['test_user03'], 'beginDate': 1})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']



