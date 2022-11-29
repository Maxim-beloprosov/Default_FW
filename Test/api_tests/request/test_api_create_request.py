import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Создание заявки')
class TestApiCreateRequest(ApiBase):
    def setup_method(self):
        self.APP.api_token.get_token('test_user09')

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
        assert request['ticketType'] == 'Request'
        assert request['gandivaService']['name'] == service_name
        assert request['descriptions'][0]['contentParts'][0]['text'] == description
        assert request['initiator']['id'] == self.users[initiator]['user_id']
        # TODO добавить проверки, проверять всё что было отправлено в запросе на создание (услуга, инициатор, описание)

    @allure.title('Создание заявки с обозревателем')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_create_request_with_observer_3(self):

        # Вносим в переменную обозревателя
        observer = 'test_user05'
        initiator = 'test_user09'
        service_name = 'AutomationService Тестовый Тип 1'
        description = "TestDescription AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Создаем заявку
        request = self.create_request({"observers": [observer], "serviceId": service_name, "descriptionContent": [description]})

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request["observers"][0]['id'] == self.users[observer]['user_id']
        assert request['gandivaService']['name'] == service_name
        assert request['descriptions'][0]['contentParts'][0]['text'] == description
        assert request['initiator']['id'] == self.users[initiator]['user_id']

    @allure.title('Создание заявки с согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_create_request_with_aprrover(self):

        # Вносим в переменную согласующего
        approver = 'test_user05'
        initiator = 'test_user09'
        service_name = 'AutomationService Тестовый Тип 1'
        description = "TestDescription AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Создаем заявку
        request = self.create_request({"approvers": [approver], "serviceId": service_name, "descriptionContent": [description]})

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request["agreements"][0]["approver"]['id'] == self.users[approver]['user_id']
        assert request['gandivaService']['name'] == service_name
        assert request['descriptions'][0]['contentParts'][0]['text'] == description
        assert request['initiator']['id'] == self.users[initiator]['user_id']

    @allure.title('Создание заявки с диспетчером')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_create_request_with_dispatcher(self):

        # Указываем название услуги, где есть ГО с диспетчером
        service_name = 'AutomationService Тестовый Тип 4'
        initiator = 'test_user09'
        description = "TestDescription AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Создаем заявку
        request = self.create_request({'serviceId': service_name})

        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')

        # Имя диспетчера
        dispatcher_name = 'test_Boss02'

        # Добавляем диспетчера в исполнителя
        request = self.APP.api_change_request.set_contractor(request['syncToken'], request['id'], self.users[dispatcher_name]['user_id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert request['ticketType'] == 'Request'
        assert request['gandivaService']['name'] == service_name
        assert request['descriptions'][0]['contentParts'][0]['text'] == description
        assert request['initiator']['id'] == self.users[initiator]['user_id']
        assert request['contractor']['id'] == self.users[dispatcher_name]['user_id']

    @allure.title('Создание заявки без услуги')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_request_without_service(self):

        # Создаем заявку без услуги
        request = self.APP.api_requests.post_requests({"serviceId": None})

        assert request['status'] == 400

    @allure.title('Создание заявки без авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_request_without_autorization(self):

        # Деавторизируемся
        self.APP.settings.Authorization = False

        # Создаем заявку
        request = self.APP.api_requests.post_requests({"serviceId": 'AutomationService Тестовый Тип 1'})

        assert request.status_code == 401

    @allure.title('Получить доступ в заявку пользователем не= участнику заявки')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_request_without_access(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на юзера не из участников тикета
        self.APP.api_token.get_token('test_user15')

        # Получаем информацию о заявке
        request = self.APP.api_requests.get_requests_id(request['id'])

        assert request['status'] == 403
