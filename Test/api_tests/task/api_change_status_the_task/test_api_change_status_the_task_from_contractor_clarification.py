import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "На уточнении у исп."')
class TestApiChangeStatusTheTaskFromContractorClarification(ApiBase):

    @allure.title('Смена статуса с "На уточнении у исп." на "В работе" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_contractor_clarification_to_work(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у исп." на "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_contractor_clarification_to_reject(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Отклоняем задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Смена статуса с "На уточнении у исп." на "На уточнении у иниц."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_contractor_clarification_to_initiator_clarification(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение исполнителю
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "На уточнении у исп." на "Ожидает до" при ответе на вопрос-уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_contractor_clarification_to_waiting(self):
        # Создаем задачу с согласующим и датой начала
        task = self.create_task({"approvers": ['test_user03'], 'beginDate': 1})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Задаем вопрос-уточнение исполнителю
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Отвечаем на вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_contractor_answer_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На уточнении у исп." на "На согласовании" при ответе на вопрос-уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_contractor_clarification_to_agreement_first(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение исполнителю
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Отвечаем на вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_contractor_answer_in_task(task['clarifications'][0]['id'], task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "На уточнении у исп." на "На согласовании" при 2-х согласующих')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_contractor_clarification_to_agreement_second(self):
        # Создаем задачу с 2-мя согласующими
        task = self.create_task({"approvers": ['test_user03', 'test_user08']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user08')
        # Задаем вопрос-уточнение исполнителю
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']



