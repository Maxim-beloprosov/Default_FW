import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API - Request')
@allure.story('Изменение статуса заявки из статуса "На уточнении у исполнителя"')
class TestChangeStatusContractorClarification(G1ApiBase):

    @allure.title('Смена статуса с "На уточнении у исполнителя" на "На согласовании", когда исполнитель ответил на вопрос-уточнение,'
                  'есть согласующий, не принявший решение по согласованию.')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_contractor_clarification_to_on_agreement(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Перелогиниваемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user['Id'])

        # Перелогиниваемся согласующим
        self.APP.g1_api_token.get_token('User5')

        # Задаем уточнение согласующим исполнителю
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение исполнителю'])

        # Перелогиниваемся исполнителем
        self.APP.g1_api_token.get_token('User2')

        # Отвечаем на уточнение исполнителем
        request = self.APP.g1_api_actions_in_request.add_clarification_answer_in_request(request['Comment']['Id'])

        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']