import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Изменение статуса заявки из статуса "На уточнении у исполнителя"')
class TestApiChangeStatusTheRequestFromContractorClarification(ApiBase):

    @allure.title('Смена статуса с "На уточнении у исполнителя" на "В работе", когда исполнитель отвечает на уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_contractor_clarification_to_work_first(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        contractor = 'test_user01'
        # Авторизуемся участником ГО
        self.APP.api_token.get_token(contractor)

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Задаем уточнение согласующим исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)

        # Отвечаем на уточнение исполнителем
        request = self.APP.api_clarifications.contractor_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у исполнителя" на "В работе", когда согласующий принял положительное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_contractor_clarification_to_work_second(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение согласующим исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "Отменено", когда исполнитель не назначен')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_contractor_clarification_to_cancel(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение согласующим исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Отменяем заявку
        request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отменено']

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "В ожидании", когда исполнитель ответил на уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_contractor_clarification_to_waiting(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver], "beginDate": 7})

        contractor = 'test_user01'
        # Авторизуемся участником ГО
        self.APP.api_token.get_token(contractor)

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Задаем уточнение согласующим исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)

        # Отвечаем на уточнение исполнителем
        request = self.APP.api_clarifications.contractor_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "На согласовании", когда исполнитель ответил на уточнение при активном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_contractor_clarification_to_agreement(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        contractor = 'test_user01'
        # Авторизуемся участником ГО
        self.APP.api_token.get_token(contractor)

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение согласующим исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Авторизуемся исполнителем
        self.APP.api_token.get_token(contractor)

        # Отвечаем на уточнение исполнителем
        request = self.APP.api_clarifications.contractor_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "На уточнении у Исполнителя" на "Отклонено", когда согласующий принял отрицательное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_contractor_clarification_to_rejected(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение согласующим исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        # Принимаем отрицательное решение согласующим
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']