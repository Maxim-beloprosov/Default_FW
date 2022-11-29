import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка смена статуса из статуса "Проверка выполнения" - Task')
class TestApiChangeStatusTaskFromResolved(G1ApiBase):

    @allure.title('Смена статуса с "Проверка выполнения" на "В работе" при возвращении на доработку')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_task_from_resolved_to_work(self):

        # Создаем задачу
        task = self.g1_create_task({"NewContractor": 'test_user2'})

        # Перелогиниваемся на исполнителя
        self.APP.g1_api_token.get_token('User2')

        # Отправляем задачу на проверку
        task = self.APP.g1_api_actions_in_task.g1_resolve_task(task['Id'], task['LastModifiedDate'])

        # Перелогиниваемся на инициатора
        self.APP.g1_api_token.get_token()

        # Возвращаем задачу на доработку
        task = self.APP.g1_api_actions_in_task.g1_back_task_to_work(task['Id'], task['LastModifiedDate'])

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']

    test_data = [1, 2, 3, 4, 5]

    @allure.title('Смена статуса с "Проверка выполнения" на "Закрыта" при оценке')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.parametrize('rating', test_data)
    def test_api_change_status_task_from_resolved_to_closed(self, rating):

        # Создаем задачу
        task = self.g1_create_task({"NewContractor": 'test_user2'})

        # Перелогиниваемся на исполнителя
        self.APP.g1_api_token.get_token('User2')

        # Отправляем задачу на проверку
        task = self.APP.g1_api_actions_in_task.g1_resolve_task(task['Id'], task['LastModifiedDate'])

        # Перелогиниваемся на инициатора
        self.APP.g1_api_token.get_token()

        # Оцениваем задачу
        task = self.APP.g1_api_actions_in_task.g1_rate_and_close_task(task['Id'], task['LastModifiedDate'], rating)

        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Закрыта']

