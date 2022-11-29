import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Эскалация заявок')
class TestApiEscalateRequest(ApiBase):

    @allure.title('Эскалация заявки с назначением заявки на участника ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_escalate_request_with_contractor(self):

        # Создаем заявку
        request = self.create_request({"serviceId": 'AutomationService Тестовый Тип 20'})

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Эскалируем заявку
        request = self.APP.api_change_request.escalate_request(request['id'], request['syncToken'])

        assert 'Группа_тестирования_№2' == request['responsibilityGroup']['name']
        assert self.APP.group_data.service_template['AutomationService Тестовый Тип 20']['serviceResponsibilityGroups'][1]['timeNormative'] == \
               request['responsibilityGroup']['plannedTimeOfExecution']
        assert 'contractor' not in request

    @allure.title('Эскалация заявки без назначения заявки на участника ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_escalate_request_without_contractor(self):

        # Создаем заявку
        request = self.create_request({"serviceId": 'AutomationService Тестовый Тип 20'})

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Эскалируем заявку
        request = self.APP.api_change_request.escalate_request(request['id'], request['syncToken'])

        assert 'Группа_тестирования_№2' == request['responsibilityGroup']['name']
        assert self.APP.group_data.service_template['AutomationService Тестовый Тип 20']['serviceResponsibilityGroups'][1]['timeNormative'] == \
               request['responsibilityGroup']['plannedTimeOfExecution']

    test_data = [
        1, 2, 3, 4, 5, 6
    ]

    @allure.title('Отсутствие возможности эскалации в статусе отличном от "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    @pytest.mark.parametrize("action_id", test_data)
    def test_escalate_request_different_status(self, action_id):

        # Создаем заявку
        request = self.create_request({"serviceId": 'AutomationService Тестовый Тип 20'})

        # Статус "На согласовании"
        if action_id == 1:
            # Добавляем согласующего для смены статуса заявки
            request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_Boss03')

        # Статус "Отменено"
        if action_id == 2:
            # Отменяем заявку
            request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Статус "В проверке"
        if action_id == 3:
            # Авторизуемся участником ГО
            self.APP.api_token.get_token('test_user01')

            # Назначаем заявку на себя
            request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

            # Переводим заявку в проверку
            request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Статус "В ожидании"
        if action_id == 4:
            # Изменяем дату начала в заявке
            request = self.APP.api_change_request.change_begin_date(request['syncToken'], request['id'], 7)

        # Статус "На уточнении у инициатора"
        if action_id == 5:
            # Авторизуемся участником ГО
            self.APP.api_token.get_token('test_user01')

            # Задаем уточнение инициатору
            request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Получаем список доступных действий
        actions = self.APP.api_requests.get_requests_id_actions(request['id'])

        assert "Escalate" not in actions



