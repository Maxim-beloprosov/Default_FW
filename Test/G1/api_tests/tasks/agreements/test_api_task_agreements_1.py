import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Согласование задач')
class TestApiTaskAgreement(G1ApiBase):

    @allure.title('Подчинённый согласовывает, начальник отклоняет')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @allure.link('https://gandiva.agatgroup.com/tickets/request/3004053')
    @pytest.mark.skip(reason='Не работают иерархические согласования в задачах Gandiva1.')
    def test_api_manager_reject_after_approve(self):

        # Создаём задачу
        task = self.g1_create_task({'Approvers': ['test_Boss1', 'test_user2']})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Перелогиниваемся на начальника
        self.APP.g1_api_token.get_token('Boss1')

        # Отклоняем задачу
        task = self.APP.g1_api_actions_in_task.g1_reject_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус согласующего-подчинённого
        approver_status_1 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        # Получаем статус согласующего-начальника
        approver_status_2 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_Boss1')

        assert approver_status_1 == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert approver_status_2 == self.APP.group_data.g1_approver_status['RUS']['Отклонена']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Отменена']

    @allure.title('Подчинённый отклоняет, начальник согласовывает')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @allure.link('https://gandiva.agatgroup.com/tickets/request/3004053')
    @pytest.mark.skip(reason='Не работают иерархические согласования в задачах Gandiva1.')
    def test_api_manager_approve_after_reject(self):

        # Создаём задачу
        task = self.g1_create_task({'Approvers': ['test_Boss1', 'test_user2']})

        # Перелогиниваемся на согласующего подчинённого
        self.APP.g1_api_token.get_token('User2')

        # Отклоняем задачу
        task = self.APP.g1_api_actions_in_task.g1_reject_task(task['Id'], task['LastModifiedDate'])

        # Перелогиниваемся на начальника
        self.APP.g1_api_token.get_token('Boss1')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус согласующего-подчинённого
        approver_status_1 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        # Получаем статус согласующего-начальника
        approver_status_2 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_Boss1')

        assert approver_status_1 == self.APP.group_data.g1_approver_status['RUS']['Отклонена']
        assert approver_status_2 == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']

    @allure.title('Несколько согласующих, все принимают положительное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_three_approvers_agree(self):

        # Создаём задачу
        task = self.g1_create_task({'Approvers': ['test_user2', 'test_user3', 'test_user4']})

        # Перелогиниваемся на 1-го согласующего
        self.APP.g1_api_token.get_token('User2')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Перелогиниваемся на 2-го согласующего
        self.APP.g1_api_token.get_token('User3')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Перелогиниваемся на 3-го согласующего
        self.APP.g1_api_token.get_token('User4')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус 1-го согласующего
        approver_status_1 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        # Получаем статус 2-го согласующего
        approver_status_2 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user3')

        # Получаем статус 3-го согласующего
        approver_status_3 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user4')

        assert approver_status_1 == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert approver_status_2 == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert approver_status_3 == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']

    @allure.title('Согласование задачи одним согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_task_agreement_first(self):

        # Создаём задачу с согласующим
        task = self.g1_create_task({"Approvers": ["test_user2"]})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус согласующего
        approver_status = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        assert approver_status == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['В работе']

    @allure.title('Согласование задачи одним из согласующих')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_task_agreement_second(self):

        # Создаём задачу с двумя согласующим
        task = self.g1_create_task({"Approvers": ["test_user2", "test_user3"]})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Согласуем задачу
        task = self.APP.g1_api_actions_in_task.g1_approve_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус согласовавшего
        approver_status_1 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        # Получаем статус второго согласующего
        approver_status_2 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user3')

        assert approver_status_1 == self.APP.group_data.g1_approver_status['RUS']['Согласовано']
        assert approver_status_2 == self.APP.group_data.g1_approver_status['RUS']['Ожидает согласования']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']

    @allure.title('Отклонение задачи одним согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_task_agreement_third(self):

        # Создаём задачу с согласующим
        task = self.g1_create_task({"Approvers": ["test_user2"]})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Отклоняем задачу
        task = self.APP.g1_api_actions_in_task.g1_reject_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус отклонившего
        approver_status = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        assert approver_status == self.APP.group_data.g1_approver_status['RUS']['Отклонена']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Отменена']

    @allure.title('Отклонение задачи одним из согласующих')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_task_agreement_fourth(self):

        # Создаём задачу с согласующим
        task = self.g1_create_task({"Approvers": ["test_user2", "test_user3"]})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User2')

        # Отклоняем задачу
        task = self.APP.g1_api_actions_in_task.g1_reject_task(task['Id'], task['LastModifiedDate'])

        # Получаем статус отклонившего
        approver_status_1 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        # Получаем статус второго согласующего
        approver_status_2 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user3')

        assert approver_status_1 == self.APP.group_data.g1_approver_status['RUS']['Отклонена']
        assert approver_status_2 == self.APP.group_data.g1_approver_status['RUS']['Отклонена']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Отменена']

    @allure.title('Добавление одного и того же согласующего дважды')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_task_agreement_fifth(self):

        # Создаём задачу с согласующим
        task = self.g1_create_task({"Approvers": ["test_user2"]})

        # Получаем профиль согласующего
        approver = self.APP.g1_api_users.get_users_profile({'login': self.APP.group_data.g1_users['User2']['Login']})

        # Добавляем согласующего в задачу
        task = self.APP.g1_api_actions_in_task.g1_add_approver_in_task(task['Id'], [approver['Id']], task['LastModifiedDate'])

        # Получаем статус согласовавшего
        approver_status_1 = self.APP.g1_api_actions_in_task.g1_get_approver_status_in_task(task['Approvers'], 'test_user2')

        assert approver_status_1 == self.APP.group_data.g1_approver_status['RUS']['Ожидает согласования']
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['На согласовании']
        assert len(task['Approvers']) == 1
