import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Изменение статуса заявки из статуса "Новая"')
class TestApiChangeStatusTheRequestFromNew(ApiBase):

    @allure.title('Смена статуса с "Новая" на "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_new_to_work(self):

        # Создаем заявку
        request = self.create_request()

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена статуса с "Новая" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_new_to_agreement(self):

        # Создаем заявку
        request = self.create_request({"approvers": ['test_user05']})

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Смена статуса с "Новая" на "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.skip  # Пока нет тестовой услуги заявка по телефону
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_new_to_resolved(self):

        # Ищем нужную услугу
        service = self.APP.api_search_services_and_catalog.search_service(
            self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])

        # Подготовка данных для создания заявки
        description = "TestDescription AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Получаем информацию об авторизованном пользователе
        autorizated_user = self.APP.api_users.get_users_profile()

        # Формируем тело запроса для создания заявки
        request_body = {
            "serviceId": service["items"][0]['id'],
            "descriptionContent": [
                {"type": "Text",
                 "text": description}
            ],
            "initiatorId": autorizated_user['id']
        }
        # Создаем заявку
        request = self.APP.api_requests.post_requests_phone(request_body)

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В проверке']

    @allure.title('Смена статуса с "Новая" на "В ожидании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_status_in_request_from_new_to_waiting(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']