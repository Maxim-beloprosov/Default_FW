import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API - Request')
@allure.story('Изменение статуса заявки из статуса "На согласовании"')
class TestChangeStatusRequestFromAgreement(G1ApiBase):

    @allure.title('Смена статуса с "На согласовании" на "В работе", когда согласующий принимает положительное решение')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_work(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User5')

        # Принимаем положительное решение согласующим
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Согласовать'])

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Смена статуса с "На согласовании" на "Отменено", когда инициатор отменяет заявку до назначения исполнителя')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_cancel(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Отменяем заявку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отменить заявку'],
                                                                        'API Test request cancel')

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Отменено']

    @allure.title('Смена статуса с "На согласовании" на "В ожидании + дата"')  # дата в формате 2022-06-08T21:00:00Z
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_waiting(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}, "RequiredStartDate": 1})

        # Авторизуемся согласующим
        self.APP.g1_api_token.get_token('User5')

        # Принимаем положительное решение согласующим
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Согласовать'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Ожидает']

    @allure.title('Смена статуса с "На согласовании" на "Отклонено"')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_rejected(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token('User5')

        # Принимаем отрицательное решение согласующим
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отклонить'],
                                                                        'API Test request reject')

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Отклонена']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_initiator_clarification_first(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение участником ГО инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                    self.APP.group_data.g1_clarification_type['RUS']
                                                                                    ['Уточнение инициатору'])

        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На уточнении']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_initiator_clarification_second(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user = self.APP.g1_api_users.get_users_profile({"Login": {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user['Id'])

        # Задаем уточнение исполнителем инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На уточнении']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Инициатора", когда уточнение задает согласующий не принявший решение')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_initiator_clarification_third(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User2']['Login']}})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение согласующим инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На уточнении']

    @allure.title('Смена статуса с "На согласовании" на "На уточнении у Исполнителя", когда уточнение задает согласующий не принявший решение')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_agreement_to_contractor_clarification(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user = self.APP.g1_api_users.get_users_profile({"Login": {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user['Id'])

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User5')

        # Задаем уточнение согласующим исполнителю
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение исполнителю'])

        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На уточнении у исполнителя']