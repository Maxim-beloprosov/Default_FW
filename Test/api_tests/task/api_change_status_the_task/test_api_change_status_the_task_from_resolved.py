import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "В проверке"')
class TestApiChangeStatusTheTaskFromResolved(ApiBase):

    @allure.title('Смена статуса с "В проверке" на "В работе" при отправке на доработку инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_task_from_resolved_to_work_second(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся под исполнителем
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу на проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Перелогиниваемся под инициатором
        self.APP.api_token.get_token('test_user09')
        # Отправляем задачу на доработку
        task = self.APP.api_actions_in_task.return_task_to_rework(task['syncToken'], task['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    test_data = [1, 2, 3, 4, 5]

    @allure.title('Смена статуса с "В проверке" на "Закрыта"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('rating', test_data)
    def test_api_change_status_in_task_from_resolved_to_closed(self, rating):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу на проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Закрываем задачу с определенной оценкой
        task = self.APP.api_actions_in_task.close_task(rating, task['syncToken'], task['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Закрыта']