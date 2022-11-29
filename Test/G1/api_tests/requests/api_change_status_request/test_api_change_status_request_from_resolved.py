import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API - Request')
@allure.story('Изменение статуса заявки из статуса "В проверке"')
class TestChangeStatusRequestFromResolved(G1ApiBase):

    @allure.title('Смена статуса с "В проверке" на "В работе", когда инициатор возвращает заявку на доработку')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_of_request_from_resolved_to_work_first(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Авторизуемся участником ГО
        self.APP.g1_api_token.get_token('User1')

        # Назначаем заявку на себя
        user = self.APP.g1_api_users.get_users_profile({"Login": {self.APP.group_data.g1_users['User1']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user['Id'])

        # Переводим заявку в проверку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отправить на проверку'])

        # Авторизуемся инициатором
        self.APP.g1_api_token.get_token()

        # Возвращаем заявку на доработку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Вернуть на доработку'],
                                                                        "Return request")

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Смена статуса с "В проверке" на "В работе", когда исполнитель возвращает заявку в работу')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_api_change_status_in_request_from_resolved_to_work_second(self):

        # Создаем заявку
        request = self.g1_create_request()

        # Перелогиниваемся участником ГО
        self.APP.g1_api_token.get_token('User1')

        # Назначаем заявку на себя
        user = self.APP.g1_api_users.get_users_profile({"Login": {self.APP.group_data.g1_users['User1']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user['Id'])

        # Переводим заявку в проверку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отправить на проверку'])

        # Возвращаем заявку в работу исполнителем
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Взять в работу'])

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    test_data = [1, 2, 3, 4, 5]

    @allure.title('Смена статуса с "В проверке" на "Закрыта"')
    @allure.description('Макаров Кирилл Геннадьевич')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.parametrize('rating', test_data)
    def test_api_change_status_in_request_from_resolved_to_closed(self, rating):

        # Создаем заявку
        request = self.g1_create_request()

        # Перелогиниваемся участником ГО
        self.APP.g1_api_token.get_token('User2')

        # Назначаем заявку на себя
        user = self.APP.g1_api_users.get_users_profile({"Login": {self.APP.group_data.g1_users['User2']['Login']}})
        request = self.APP.g1_api_actions_in_request.update_contractor_in_request(request['Id'], request['LastModifiedDate'], user['Id'])

        # Переводим заявку в проверку
        request = self.APP.g1_api_actions_in_request.actions_in_request(request['Id'], request['LastModifiedDate'],
                                                                        self.APP.group_data.g1_tickets_actions['RUS']['Отправить на проверку'])

        # Перелогиниваемся инициатором
        self.APP.g1_api_token.get_token()

        # Закрываем заявку нужной оценкой
        request = self.APP.g1_api_actions_in_request.g1_rate_and_close_request(request['Id'], request['LastModifiedDate'], rating)

        assert request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Закрыта']
