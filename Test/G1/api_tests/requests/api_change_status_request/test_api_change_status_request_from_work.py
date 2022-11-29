import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API - Request')
@allure.story('Изменение статуса заявки из статуса "В работе"')
class TestChangeStatusRequestFromInWork(G1ApiBase):

    @allure.title('Смена статуса с "В работе" на "Отменено", когда исполнитель не назначен')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_work_to_cancel(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Отменяем заявку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отменить заявку'],
                                                                        'Cancel request')

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Отменено']

    @allure.title('Смена статуса с "В работе" на "В проверке"')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_work_to_resolved(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО будущей заявки
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user_info['Id'])

        # Переводим заявку в проверку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отправить на проверку'])

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Проверка выполнения']

    @allure.title('Смена статуса с "В работе" на "В ожидании"')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_work_to_waiting(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Подготавливаем дату
        date = self.APP.time.get_date_increased_x_days_json(1)

        # Изменяем дату начала в заявке
        request = self.APP.g1_api_actions_in_request.change_request_start_date(request['Id'], request['LastModifiedDate'], date)

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Ожидает']

    @allure.title('Смена статуса с "В работе" на "На согласовании"')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_work_to_agreement(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Добавляем согласующего
        user_info = self.APP.g1_api_users.get_users_profile({'Login': {self.APP.group_data.g1_users['User5']['Login']}})
        request = self.APP.g1_api_actions_in_request.put_add_approver(request['Id'], request['LastModifiedDate'], [user_info['Id']])

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']

    @allure.title('Смена статуса с "В работе" на "На уточнении у Инициатора", когда уточнение задает участник ГО')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_work_to_initiator_clarification_first(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Задаем уточнение инициатору
        request = self.APP.g1_api_actions_in_request.add_clarification_question_in_request(request['Id'],
                                                                                           self.APP.group_data.g1_clarification_type['RUS']
                                                                                           ['Уточнение инициатору'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['RequestStatus'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На уточнении']

    @allure.title('Смена статуса с "В работе" на "На уточнении у Инициатора", когда уточнение задает исполнитель')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_work_to_initiator_clarification_second(self):

        # Создаем заявку
        request = self.g1_create_request()

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