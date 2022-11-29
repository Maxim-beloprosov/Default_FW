import time

import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Счётчики времени')
class TestApiRequestTimeCounters(ApiBase):

    @allure.title('Фактическое время исполнения(ГО)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/21889/')
    @pytest.mark.skip(reason='API. ЗЯ. СЧ. Не работает счётчик времени исполнения ГО')
    def test_factual_rg_execution_time_request(self):

        # Создаем заявку
        request = self.create_request()

        time.sleep(65)

        # Обновляем данные заявки
        request = self.APP.api_requests.get_requests_id(request['id'])

        assert self.APP.api_actions_in_request.check_factual_time(request['counters'], 'ResponsibilityGroupExecution', 1)
        assert self.APP.api_actions_in_request.check_equal_target_id(request['counters'], 'ResponsibilityGroupExecution', request['responsibilityGroup']['id'])
        assert request['navigator']['execution']['timeNavigatorStatus'] == 'Active'

    @allure.title('Фактическое время исполнения(Исполнитель)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_factual_contractor_execution_time_request(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        time.sleep(65)

        # Обновляем данные заявки
        request = self.APP.api_requests.get_requests_id(request['id'])

        assert self.APP.api_actions_in_request.check_factual_time(request['counters'], 'ContractorExecution', 1)
        assert self.APP.api_actions_in_request.check_equal_target_id(request['counters'], 'ContractorExecution', request['contractor']['id'])
        assert request['navigator']['execution']['timeNavigatorStatus'] == 'Active'

    @allure.title('Фактическое время согласования(общее)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_factual_agreement_time_request(self):

        # Создаем заявку
        request = self.create_request({'approvers': ['test_user01']})

        time.sleep(65)

        # Обновляем данные заявки
        request = self.APP.api_requests.get_requests_id(request['id'])

        assert self.APP.api_actions_in_request.check_factual_time(request['counters'], 'TotalAgreement', 1)
        assert request['navigator']['agreement']['timeNavigatorStatus'] == 'Active'

    @allure.title('Фактическое время согласования(конкретного согласующего)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_factual_agreement_time_request_second(self):

        # Создаем заявку
        request = self.create_request({'approvers': ['test_user01', 'test_user02']})

        time.sleep(65)

        # Обновляем данные заявки
        request = self.APP.api_requests.get_requests_id(request['id'])

        # Получаем id согласования для одного из согласующих
        agreement_id = self.agreement_id(request['agreements'], self.APP.group_data.users['test_user01']['user_id'])

        assert self.APP.api_actions_in_request.check_factual_time(request['counters'], 'PendingAgreement', 1)
        assert self.APP.api_actions_in_request.check_equal_target_id(request['counters'], 'PendingAgreement', agreement_id)
        assert request['navigator']['agreement']['timeNavigatorStatus'] == 'Active'

    @allure.title('Фактическое время оценки заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_factual_feedback_time_request(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Отправляем заявку на проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        time.sleep(65)

        # Обновляем данные заявки
        request = self.APP.api_requests.get_requests_id(request['id'])

        assert self.APP.api_actions_in_request.check_factual_time(request['counters'], 'Feedback', 1)

    @allure.title('Фактическое время ожидания')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_factual_waiting_time_request(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        time.sleep(65)

        # Обновляем данные заявки
        request = self.APP.api_requests.get_requests_id(request['id'])

        assert self.APP.api_actions_in_request.check_factual_time(request['counters'], 'Waiting', 1)
