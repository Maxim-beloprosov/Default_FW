import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка смена статуса из статуса "Ожидает" - Task')
class TestApiChangeStatusTaskFromWaiting(G1ApiBase):

    @allure.title('Смена статуса с "Ожидает" на "На согласовании" при добавлении согласующего инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_waiting_to_agreement_first(self):
        # Получаем профиль согласующего
        approver = self.APP.g1_api_users.get_users_profile({'login': 'test_user3'})

        # Создаем задачу
        task = self.g1_create_task({"RequiredStartDate": 1})

        # Приводим id согласующего к нужному типу
        approvers_id = [approver['Id']]

        # Добавляем согласующего в задачу
        task = self.APP.g1_api_actions_in_task.g1_add_approver_in_task(task['Id'], approvers_id, task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']

    @allure.title('Смена статуса с "Ожидает" на "На согласовании" при добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_waiting_to_agreement_second(self):

        # Получаем профиль согласующего
        approver = self.APP.g1_api_users.get_users_profile({'login': 'test_user3'})

        # Создаем задачу
        task = self.g1_create_task({"RequiredStartDate": 1, "NewContractor": 'test_user2'})

        # Перелогиниваемся на исполнителя
        self.APP.g1_api_token.get_token('User2')

        # Приводим id согласующего к нужному типу
        approvers_id = [approver['Id']]

        # Добавляем согласующего в задачу
        task = self.APP.g1_api_actions_in_task.g1_add_approver_in_task(task['Id'], approvers_id, task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']

    @allure.title('Смена статуса с "Ожидает" на "В работе" при изменении даты начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_waiting_to_work(self):

        # Создаем задачу
        task = self.g1_create_task({"RequiredStartDate": 1})

        date = self.APP.time.get_date_increased_x_days_json(0)

        task = self.APP.g1_api_actions_in_task.g1_change_task_start_date(task['Id'], task['LastModifiedDate'], date)

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']



