import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - test')
@allure.story('Создание заявки')
class TestApiCreateRequest(ApiBase):

    @allure.title('Создание заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_create_request(self):

        # Готовим данные для создания заявки
        initiator = 'test_user09'
        service_name = 'AutomationService Тестовый Тип 1'
        description = "TestDescription AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Создаем заявку
        request = self.create_request({"serviceId": service_name, "descriptionContent": [description]})

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'test'
        assert request['gandivaService']['name'] == service_name
        assert request['descriptions'][0]['contentParts'][0]['text'] == description
        assert request['initiator']['id'] == self.users[initiator]['user_id']
