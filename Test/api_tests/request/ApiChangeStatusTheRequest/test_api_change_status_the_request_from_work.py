import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - request')
@allure.story('Изменение статуса заявки из статуса "В работе"')
class TestApiChangeStatusTheRequestFromWork(ApiBase):

    @allure.title('Смена статуса с "В работе" на "Отменено", когда исполнитель не назначен')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_cancel_first(self):

        # Создаем заявку
        request = self.create_request()

        # Отменяем заявку
        request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отменено']

    @allure.title('Смена статуса с "В работе" на "Отменено", когда инициатор РАВЕН исполнителю')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_cancel_second(self):

        # Авторизуемся участником ГО будущей заявки
        self.APP.api_token.get_token('test_user01')

        # Создаем заявку
        request = self.create_request()

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Отменяем заявку
        request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отменено']

    @allure.title('Смена статуса с "В работе" на "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_resolved(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Переводим заявку в проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В проверке']

    @allure.title('Смена статуса с "В работе" на "В ожидании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_waiting(self):

        # Создаем заявку
        request = self.create_request()

        # Изменяем дату начала в заявке
        request = self.APP.api_change_request.change_begin_date(request['syncToken'], request['id'], 7)

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "В работе" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_agreement(self):

        # Создаем заявку
        request = self.create_request()

        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user05')

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "В работе" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_initiator_clarification_first(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "В работе" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_work_to_initiator_clarification_second(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

