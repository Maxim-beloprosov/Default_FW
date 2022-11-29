import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - request')
@allure.story('Изменение статуса заявки из статуса "Отклонено"')
class TestApiChangeStatusTheRequestFromRejected(ApiBase):

    @allure.title('Смена статуса с "Отклонено" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_rejected_to_agreement(self):

        approver = 'test_user05'

        # Создаем заявку
        request = self.create_request({"approvers": [approver]})

        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)

        # Принимаем отрицательное решение согласующим
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Апеллируем заявку
        request = self.APP.api_actions_in_request.appeal_request(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']