import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "На уточнении у иниц."')
class TestApiChangeStatusTheTaskFromInitiatorClarification(ApiBase):

    @allure.title('Смена статуса с "На уточнении у иниц." на "В работе" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_initiatior_clarification_to_work_first(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у иниц." на "В работе" при отмене вопроса-уточнения исполнителя')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_initiatior_clarification_to_work_second(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Отменяем вопрос уточнение
        task = self.APP.api_actions_in_task.cancel_initiator_clarification_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
         # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у иниц." на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_initiator_clarification_to_agreement(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Отвечаем на вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_initiator_answer_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "На уточнении у иниц." на "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_initiator_clarification_to_reject(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Отклоняем задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Смена статуса с "На уточнении у иниц." на "На уточнении у исп."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_initiator_clarification_to_contractor_clarification(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Задаем вопрос-уточнение исполнителю
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Отвечаем на вопрос-уточнение инициатора
        task = self.APP.api_actions_in_task.clarification_initiator_answer_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у исп.']

    @allure.title('Смена статуса с "На уточнении у иниц." на "Ожидает до" при ответе инициатором на вопрос-уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_initiator_clarification_to_waiting_first(self):
        # Создаем задачу с согласующим и датой начала
        task = self.create_task({"approvers": ['test_user03'], 'beginDate': 1})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Отвечаем на вопрос-уточнение инициатора
        task = self.APP.api_actions_in_task.clarification_initiator_answer_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На уточнении у иниц." на "Ожидает до" при отмене вопроса-уточнения исполнителя')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_initiator_clarification_to_waiting_second(self):
        # Создаем задачу с датой начала
        task = self.create_task({"beginDate": 1})
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Отменяем вопрос-уточнение
        task = self.APP.api_actions_in_task.cancel_initiator_clarification_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']
