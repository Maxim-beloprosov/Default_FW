import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Добавление согласующего"')
class TestApiAddApproverInTheRequest(ApiBase):

    @allure.title('Инициатор добавляет согл. при создании')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_create_request_with_agreement(self):
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_user01']})
        # Сравниваем полученные значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Инициатор добавляет согл. после создания заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_first(self):
        # Создаем заявку
        request = self.create_request()
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user01')
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Модератор добавляет исполнителя, исполнитель добавляет согласующего')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_second(self):
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем исполнителя
        request = self.APP.api_change_request.set_contractor(request['syncToken'], request['id'], self.users['test_Boss01']['user_id'])
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user01')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Согласующий добавляется из услуги')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_third(self):
        # Создаем заявку
        request = self.create_request({'serviceId': self.APP.group_data.service_template['AutomationService Тестовый Тип 2']['name']})
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Согласующий добавляется при смене услуги модератором')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_fourth(self):
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Ищем нужную услугу
        services = self.APP.api_actions_in_service_catalog.search_service(self.APP.group_data.service_template['AutomationService Тестовый Тип 2']['name'])
        # Обновляем услугу
        request = self.APP.api_change_request.change_service_in_request(request['syncToken'], request['id'], services["items"][0]['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Инициатор заявки является обязат. согласующим в нормативе')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_fifth(self):
        # Перелогиниваемся на пользователя, который является обязательным согласующим
        self.APP.api_token.get_token('test_Boss01')
        # Создаем заявку
        request = self.create_request(
            {'serviceId': self.APP.group_data.service_template['AutomationService Тестовый Тип 2']['name']})
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']
        assert request['agreements'] == []

    @allure.title('Инициатор дважды добавляет одного и того же согласующего')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_sixth(self):
        # Создаем заявку
        request = self.create_request()
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_Boss03')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_Boss03')
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert len(request['agreements']) == 1

    @allure.title('Исполнитель добавляет согласующего')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_in_the_request_seventh(self):
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_Boss01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_Boss03')
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']



