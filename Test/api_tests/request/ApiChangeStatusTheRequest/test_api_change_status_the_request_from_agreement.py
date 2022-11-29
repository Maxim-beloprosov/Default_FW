import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - request')
@allure.story('Изменение статуса заявки из статуса "На согласовании"')
class TestApiChangeStatusTheRequestFromWork(ApiBase):

    @allure.title('Смена статуса с "На согласовании" на "В работе", когда согласующий принимает положительное решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_change_status_in_request_from_agreement_to_work(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "На согласовании" на "Отменено", когда инициатор отменяет заявку до назначения исполнителя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_agreement_to_cancel(self):

        # Создаем заявку
        request = self.create_request({"approvers": ['test_user05']})

        # Отменяем заявку
        request = self.APP.api_actions_in_request.cancel_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отменено']

    @allure.title('Смена статуса с "На согласовании" на "В ожидании + дата"')  # дата в формате 2022-06-08T21:00:00Z
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_agreement_to_waiting(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver], "beginDate": 7})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем положительное решение согласующим
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена статуса с "На согласовании" на "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_change_status_in_request_from_agreement_to_rejected(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем отрицательное решение согласующим
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_agreement_to_initiator_clarification_first(self):

        # Создаем заявку
        request = self.create_request({"approvers": ['test_user05']})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Задаем уточнение участником ГО инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_agreement_to_initiator_clarification_second(self):

        # Создаем заявку
        request = self.create_request({"approvers": ['test_user05']})

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Задаем уточнение исполнителем инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает согласующий не принявший решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_change_status_in_request_from_agreement_to_initiator_clarification_third(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Задаем уточнение согласующим инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у иниц.']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Исполнителя", когда уточнение задает согласующий не принявший решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_change_status_in_request_from_agreement_to_contractor_clarification(self):

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

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у исп.']