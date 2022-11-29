import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API - Request')
@allure.story('Изменение статуса заявки из статуса "В ожидании"')
class TestChangeStatusRequestFromResolved(G1ApiBase):

    @allure.title('Смена статуса с "В ожидании + дата" на "В работе", когда исполнитель переводит заявку в работу')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_waiting_to_work_first(self):

        # Создаем заявку
        request = self.g1_create_request({"RequiredStartDate": 1})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user_info['Id'])

        # Берем заявку в работу
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Взять в работу'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']


    @allure.title('Смена статуса с "В ожидании + дата" на "Отменено", при отмене инициатором, если исполнитель не назначен')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_waiting_to_second(self):

        # Создаем заявку
        request = self.g1_create_request({'RequiredStartDate': 1})

        # Отменяем заявку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отменить заявку'],
                                                                        'Cancel request')

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Отменено']

    @allure.title('Смена статуса с "В ожидании + дата" на "На согласовании", при добавлении согласующего')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_waiting_to_agreement(self):

        # Создаем заявку
        request = self.g1_create_request({'RequiredStartDate': 1})

        # Добавляем согласующего
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User5']['Login']}})
        request = self.APP.g1_api_actions_in_request.put_add_approver(request['Id'], request['LastModifiedDate'], [user_info['Id']])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']

    @allure.title('Смена статуса с "В ожидании + дата" на "На уточнении у инициатора", когда уточнение задает исполнитель')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_g1_api_change_status_in_request_from_waiting_to_initiator_clarification_first(self):

        # Создаем заявку
        request = self.g1_create_request({'RequiredStartDate': 1})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user_info['Id'])

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На уточнении']

