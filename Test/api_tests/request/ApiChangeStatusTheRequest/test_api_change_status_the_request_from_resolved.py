import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Изменение статуса заявки из статуса "В проверке"')
class TestApiChangeStatusTheRequestFromResolved(ApiBase):

    @allure.title('Смена статуса с "В проверке" на "В работе", когда инициатор возвращает заявку на доработку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_resolved_to_work_first(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Переводим заявку в проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Возвращаем заявку на доработку
        request = self.APP.api_actions_in_request.comeback_ticket_to_overwork(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "В проверке" на "В работе", когда исполнитель возвращает заявку в работу')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_resolved_to_work_second(self):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Переводим заявку в проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Возвращаем заявку в работу исполнителем
        request = self.APP.api_actions_in_request.comeback_ticket_to_work(request['syncToken'], request['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    test_data = [1, 2, 3, 4, 5]

    @allure.title('Смена статуса с "В проверке" на "Закрыта"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('rating', test_data)
    def test_api_change_status_in_request_from_resolved_to_closed_first(self, rating):

        # Создаем заявку
        request = self.create_request()

        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Переводим заявку в проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')

        # Закрываем заявку нужной оценкой
        request = self.APP.api_actions_in_request.close_request(request['syncToken'], request['id'], rating)

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Закрыта']
        assert request['feedback']['rating'] == rating

