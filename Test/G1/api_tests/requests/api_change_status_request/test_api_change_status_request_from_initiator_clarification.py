import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.feature('Api - Request')
@allure.story('Изменение статуса заявки из статуса "На уточнении у инициатора"')
class TestApiChangeStatusRequestFromInitiatorClarification(G1ApiBase):

    @allure.title('Смена статуса с "На уточнении у инициатора" на "В работе", когда инициатор отвечает на уточнение')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_work_first(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Авторизуемся инициатором
        self.APP.g1_api_token.get_token()

        # Отвечаем на уточнение
        request = self.APP.g1_api_actions_in_request.add_clarification_answer_in_request(request['Comment']['Id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Смена статуса с "На уточнении у инициатора" на "В работе", когда исполнитель отменяет свое уточнение')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_work_second(self):

        # Создаем заявку
        request = self.g1_create_request()
        request_id = request['Id']

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User2']['Login']}})
        self.APP.g1_api_actions_in_request.update_contractor_in_request(request_id, request['LastModifiedDate'], user_info['Id'])

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request_id,
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Отменяем уточнение
        self.APP.g1_api_requests.post_requests_comments_id_cancel_clarification(request['Comment']['Id'])
        request = self.APP.g1_api_requests.get_requests_id(request_id)

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Смена статуса с "На уточнении у инициатора" на "В работе", когда участник ГО отменяет свое уточнение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_work_third(self):

        # Создаем заявку
        request = self.g1_create_request()
        request_id = request['Id']

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request_id,
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Отменяем уточнение
        self.APP.g1_api_requests.post_requests_comments_id_cancel_clarification(request['Comment']['Id'])
        request = self.APP.g1_api_requests.get_requests_id(request_id)

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В работе", согласующий принимает решение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_request_from_initiator_clarification_to_work_fourth(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User2']['Login']}})

        # Авторизуемся согласующим
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        request1 = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                            self.APP.group_data.g1_clarification_type['RUS']
                                                                                            ['Уточнение инициатору'])

        # Принимаем положительное решение согласующим
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request1['LastModifiedDate'], self.APP.group_data.g1_tickets_actions['RUS']['Согласовать'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Смена статуса с "На уточнении у инициатора" на "Отменено", когда инициатор отменяет заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_cancel(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        request1 = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                            self.APP.group_data.g1_clarification_type['RUS']
                                                                                            ['Уточнение инициатору'])

        # Авторизуемся инициатором
        self.APP.g1_api_token.get_token()

        # Отменяем заявку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request1['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отменить заявку'],
                                                                        'Cancel request')

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Отменено']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В ожидании + дата", когда инициатор отвечает на уточнение и есть дата начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_waiting_first(self):

        # Создаем заявку
        request = self.g1_create_request({"RequiredStartDate": 1})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Авторизуемся инициатором
        self.APP.g1_api_token.get_token()

        # Отвечаем на уточнение
        request = self.APP.g1_api_actions_in_request.add_clarification_answer_in_request(request['Comment']['Id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Ожидает']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В ожидании + дата", когда исполнитель отменяет уточнение и есть дата начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_request_from_initiator_clarification_to_waiting_second(self):

        # Создаем заявку
        request = self.g1_create_request({"RequiredStartDate": 1})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User2']['Login']}})
        self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user_info['Id'])

        # Задаем уточнение инициатору
        request1 = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                            self.APP.group_data.g1_clarification_type['RUS']
                                                                                            ['Уточнение инициатору'])

        # Отменяем уточнение
        self.APP.g1_api_requests.post_requests_comments_id_cancel_clarification(request1['Comment']['Id'])

        # Авторизуемся инициатором
        self.APP.g1_api_token.get_token()

        # Получаем данные о заявке
        request = self.APP.g1_api_requests.get_requests_id(request['Id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Ожидает']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "В ожидании + дата", когда участник ГО отменяет уточнение и есть дата начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_waiting_third(self):

        # Создаем заявку
        request = self.g1_create_request({"RequiredStartDate": 1})

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        question = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                            self.APP.group_data.g1_clarification_type['RUS']
                                                                                            ['Уточнение инициатору'])

        # Отменяем уточнение
        self.APP.g1_api_requests.post_requests_comments_id_cancel_clarification(question['Comment']['Id'])

        # Получаем данные о заявке
        request = self.APP.g1_api_requests.get_requests_id(request['Id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Ожидает']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_initiator_clarification_to_agreement(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User5']['Login']}})

        # Авторизуемся согласующим
        self.APP.g1_api_token.get_token('User5')

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Авторизуемся инициатором
        self.APP.g1_api_token.get_token()

        # Отвечаем на уточнение
        request = self.APP.g1_api_actions_in_request.add_clarification_answer_in_request(request['Comment']['Id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']

    @allure.title('Смена статуса с "На уточнении у Инициатора" на "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_request_from_initiator_clarification_to_rejected(self):

        # Создаем заявку
        request = self.g1_create_request({"Approvers": {self.APP.group_data.g1_users['User2']['Login']}})

        # Авторизуемся согласующим
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        clarification_question = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                                          self.APP.group_data.g1_clarification_type['RUS']
                                                                                                          ['Уточнение инициатору'])

        # Принимаем отрицательное решение согласующим
        request1 = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], clarification_question['LastModifiedDate'],
                                                                         self.APP.group_data.g1_tickets_actions['RUS']['Отклонить'], 'Reject request')

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request1['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Отклонена']