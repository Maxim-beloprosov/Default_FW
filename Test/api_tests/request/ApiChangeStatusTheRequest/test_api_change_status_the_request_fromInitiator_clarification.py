import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Изменение статуса заявки из статуса "На уточнении у инициатора"')
class TestApiChangeStatusTheRequestFromInitiatorClarification(ApiBase):

    @allure.title('Смена статуса с "На уточнении у инициатора" на "В работе", когда инициатор отвечает на уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_work_first(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Отвечаем на уточнение
        request = self.APP.api_clarifications.initiator_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у инициатора" на "В работе", когда исполнитель отменяет свое уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_work_second(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Отменяем уточнение
        request = self.APP.api_clarifications.cancel_clarifications(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у инициатора" на "В работе", когда участник ГО отменяет свое уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_work_third(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Отменяем уточнение
        request = self.APP.api_clarifications.cancel_clarifications(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В работе", согласующий принимает решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_work_fourth(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у инициатора" на "Отменено", когда инициатор отменяет заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_cancel(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Отменяем заявку
        request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отменено']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В ожидании + дата", когда инициатор отвечает на уточнение и есть дата начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_waiting_first(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Отвечаем на уточнение
        request = self.APP.api_clarifications.initiator_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В ожидании + дата", когда исполнитель отменяет уточнение и есть дата начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_waiting_second(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Отменяем уточнение
        request = self.APP.api_clarifications.cancel_clarifications(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В ожидании + дата", когда участник ГО отменяет уточнение и есть дата начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_waiting_third(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Отменяем уточнение
        request = self.APP.api_clarifications.cancel_clarifications(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_agreement(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Отвечаем на уточнение
        request = self.APP.api_clarifications.initiator_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_initiator_clarification_to_rejected(self):
        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token('test_user05')

        # Задаем уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Принимаем отрицательное решение согласующим
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']