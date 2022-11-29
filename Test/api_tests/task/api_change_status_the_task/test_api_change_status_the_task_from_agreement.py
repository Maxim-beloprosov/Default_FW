import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "На согласовании"')
class TestApiChangeStatusTheTaskFromAgreement(ApiBase):

    @allure.title('Смена статуса с "На согласовании" на "В работе" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_agreement_to_work_first(self):
        # Создаем задачу
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На согласовании" на "Ожидает до" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_agreement_to_waiting_first(self):
        # Создаем задачу
        task = self.create_task({"approvers": ['test_user03'], 'beginDate': 1})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На согласовании" на "Отклонено" при отрицательном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_agreement_to_rejected(self):
        # Создаем задачу
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Отклоняем задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у иниц."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_agreement_to_initiator_clarification(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у исп."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_agreement_to_contractor_clarification(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у исп.']

    @allure.title('Смена статуса с "На согласовании" на "Ожидает до" при удалении согласования модератором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_agreement_to_waiting_second(self):
        # Создаем задачу с согласующим и датой начала
        task = self.create_task({"approvers": ['test_user03'], 'beginDate': 1})
        # Перелогиниваемся под модератора
        self.APP.api_token.get_token('SystemOperator')
        # Удаляем согласование
        task = self.APP.api_tasks.delete_tasks_id_agreements_agreement_id(task['id'], task['agreements'][0]['id'], params={'isModeratorMode': True})
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На согласовании" на "В работе" при удалении согласования модератором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_agreement_to_work_second(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся под модератора
        self.APP.api_token.get_token('SystemOperator')
        # Удаляем согласование
        task = self.APP.api_tasks.delete_tasks_id_agreements_agreement_id(task['id'], task['agreements'][0]['id'], 'isModeratorMode=true')
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']
