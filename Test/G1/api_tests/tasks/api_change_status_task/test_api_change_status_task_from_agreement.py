import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка смена статуса из статуса "В работе" - Task')
class TestApiChangeStatusTaskFromAgreement(G1ApiBase):

    @allure.title('Смена статуса с "На согласовании" на "В работе" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_agreement_to_work(self):

        # Создаем задачу
        task = self.g1_create_task({"Approvers": ['test_user2']})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']

    @allure.title('Смена статуса с "На согласовании" на "Ожидает" при положительном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_agreement_to_wait(self):

        # Создаем задачу
        task = self.g1_create_task({"Approvers": ['test_user2'], 'RequiredStartDate': 1})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Ожидает']

    @allure.title('Смена статуса с "На согласовании" на "Отменена" при отрицательном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_agreement_to_canceled(self):

        # Создаем задачу
        task = self.g1_create_task({"Approvers": ['test_user2']})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Отклоняем задачу
        task = self.APP.g1_api_actions_in_task.g1_reject_task(task['Id'], task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Отменена']

