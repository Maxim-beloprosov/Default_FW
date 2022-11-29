import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - request')
@allure.story('Изменение статуса заявки из статуса "В ожидании"')
class TestApiChangeStatusTheRequestFromWaiting(ApiBase):

    @allure.title('Смена статуса с "В ожидании + дата" на "В работе", когда инициатор удаляет дату начала в разрешенное время')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_work_first(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Обновляем заявку, удаляя дату начала
        request = self.APP.api_change_request.delete_begin_date(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "В ожидании + дата" на "В работе", когда исполнитель переводит заявку в работу')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_work_second(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Берем заявку в работу
        request = self.APP.api_actions_in_request.take_request_for_work(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "В ожидании + дата" на "Отменено", при отмене инициатором, если исполнитель не назначен')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_cancel(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Отменяем заявку
        request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отменено']

    @allure.title('Смена статуса с "В ожидании + дата" на "На согласовании", при добавлении согласующего')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_agreement(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user05')

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "В ожидании + дата" на "На уточнении у инициатора", когда уточнение задает исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_initiator_clarification_first(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "В ожидании + дата" на "На уточнении у инициатора", когда уточнение задает участник ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_initiator_clarification_second(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "В ожидании + дата" на "На уточнении у исполнителя", когда уточнение задает согласующий принявший решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_waiting_to_contractor_clarification(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver], "beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем положительное решение
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Задаем уточнение исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у исп.']