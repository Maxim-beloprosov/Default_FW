import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API - Request')
@allure.story('Изменение статуса заявки из статуса "Отклонено"')
class TestChangeStatusRequestFromRejected(G1ApiBase):

    @allure.title('Смена статуса с "Отклонено" на "На согласовании"')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_rejected_to_agreement(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Перелогиниваемся согласующим
        self.APP.g1_api_token.get_token('User5')

        # Принимаем отрицательное решение согласующим
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отклонить'])

        # Перелогиниваемся инициатором
        self.APP.g1_api_token.get_token()

        # Апеллируем заявку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Апеллировать вышестоящему'])

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']