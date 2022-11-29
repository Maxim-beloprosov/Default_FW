import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Изменение статуса задачи из статуса "Отклонено"')
class TestApiChangeStatusTheTaskFromRejected(ApiBase):

    @allure.title('Смена статуса с "Отклонено" на "На согласовании" при апелляции')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_change_status_in_task_from_rejected_to_agreement(self):
        # Создаем задачу с согласующим
        task = self.create_task({"approvers": ['test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Отклоняем задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])
        #Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Производим апелляцию
        task = self.APP.api_actions_in_task.appeal_task(task['syncToken'], task['id'])
        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

