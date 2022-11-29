import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Создание задач')
class TestCreateTask(G1ApiBase):

    @allure.title('Создание задачи на себя')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_task_assigned_to_me(self):
        # логинимся под 1 пользователем
        self.APP.g1_api_token.get_token('User1')
        # Описание для задачи
        description = 'AutomationApiTest Description'
        # заголовок для задачи
        subject = 'AutomationApiTest Subject'
        # Получаем пользователя для сравнения
        contractor = self.APP.g1_api_users.get_users_profile({'login': 'testuser1'})
        # Создаем задачу, назначаем себя исполнителем
        task = self.g1_create_task({'NewContractor': 'testuser1', 'Subject': subject, 'Description': description})
        assert task['Contractors'][0]['Id'] == contractor['Id']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']
        assert task['Subject'] == subject
        assert task['Description'] == description

    @allure.title('Создание задачи с обозревателем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_task_with_observer(self):
        # Создаем задачу с обозревателем
        task = self.g1_create_task({'Observers': [self.APP.group_data.g1_users['User2']['Login']]})
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']
        assert task['Observers'][0]['Login'] == self.APP.group_data.g1_users['User2']['Login']

    @allure.title('Создание задачи с согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_task_with_approver(self):
        # Создаем задачу с согласующим
        task = self.g1_create_task({'Approvers': [self.APP.group_data.g1_users['User2']['Login']]})
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']
        assert task['Approvers'][0]['Login'] == self.APP.group_data.g1_users['User2']['Login']


