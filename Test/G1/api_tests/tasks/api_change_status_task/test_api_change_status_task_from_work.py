import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка смена статуса из статуса "В работе" - Task')
class TestApiChangeStatusTaskFromWork(G1ApiBase):

    @allure.title('Смена статуса с "В работе" на "На согласовании" при добавлении согласующего инициатором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_work_to_agreement_first(self):

        # Получаем профиль согласующего
        approver = self.APP.g1_api_users.get_users_profile({'login': 'test_user3'})

        # Создаем задачу
        task = self.g1_create_task()

        # Приводим id согласующего к нужному типу
        approvers_id = [approver['Id']]

        # Добавляем согласующего в задачу
        task = self.APP.g1_api_actions_in_task.g1_add_approver_in_task(task['Id'], approvers_id, task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']

    @allure.title('Смена статуса с "В работе" на "На согласовании" при добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_work_to_agreement_second(self):

        # Получаем профиль согласующего
        approver = self.APP.g1_api_users.get_users_profile({'login': 'test_user3'})

        # Создаем задачу
        task = self.g1_create_task()

        # Перелогиниваемся на исполнителя
        self.APP.g1_api_token.get_token('User1')

        # Приводим id согласующего к нужному типу
        approvers_id = [approver['Id']]

        # Добавляем согласующего в задачу
        task = self.APP.g1_api_actions_in_task.g1_add_approver_in_task(task['Id'], approvers_id, task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']

    @allure.title('Смена статуса с "В работе" на "Проверка выполнения"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_work_to_resolved(self):

        # Создаем задачу
        task = self.g1_create_task()

        # Перелогиниваемся на исполнителя
        self.APP.g1_api_token.get_token('User1')

        # Отправляем задачу на проверку
        task = self.APP.g1_api_actions_in_task.g1_resolve_task(task['Id'], task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Проверка выполнения']

    @allure.title('Смена статуса с "В работе" на "Ожидает"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_work_to_wait(self):

        # Создаем задачу
        task = self.g1_create_task()

        # Подготавливаем дату
        date = self.APP.time.get_date_increased_x_days_json(1)

        # Меняем дату начала
        task = self.APP.g1_api_actions_in_task.g1_change_task_start_date(task['Id'], task['LastModifiedDate'], date)

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Ожидает']

    @allure.title('Смена статуса с "В работе" на "Отменено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_work_to_canceled(self):

        # Перелогиниваемся на User2, чтобы инициатор был = исполнителю
        self.APP.g1_api_token.get_token('User2')

        # Создаем задачу
        task = self.g1_create_task({"NewContractor": 'test_user2'})

        # Отменяем задачу
        task = self.APP.g1_api_actions_in_task.g1_cancel_task(task['Id'], task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Отменена']
