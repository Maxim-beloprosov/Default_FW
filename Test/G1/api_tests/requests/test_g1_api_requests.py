import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка создания заявки')
class TestG1ObserversInRequests(G1ApiBase):

    @allure.title('Добавление обозревателя (инициатор)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_by_initiator(self):

        # Создание заявки
        created_request = self.g1_create_request()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Добавление обозревателя в заявку.
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], created_request['LastModifiedDate'], [user02_id])

        assert add_observer['Observers'][0]['Id'] == user02_id
        assert 'RequestType' in created_request

    @allure.title('Добавление обозревателя (обозреватель)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_by_observer(self):

        # Создание заявки
        created_request = self.g1_create_request()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Добавление обозревателя в заявку.
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], created_request['LastModifiedDate'], [user02_id])

        # Переходим на обозревателя
        self.APP.g1_api_token.get_token('User2')

        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']

        # Добавление обозревателя в заявку.
        add_observer2 = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], add_observer['LastModifiedDate'], [user06_id])

        assert (add_observer2['Observers'][0]['Id'] == user06_id or add_observer2['Observers'][1]['Id'] == user06_id)
        assert 'RequestType' in created_request

    @allure.title('Добавление обозревателя (согласующий)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_by_approver(self):

        # Создание заявки
        created_request = self.g1_create_request()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Добавляем согласующего
        add_approver = self.APP.g1_api_actions_in_request.put_add_approver(created_request['Id'], created_request['LastModifiedDate'], [user02_id])

        # Переходим на пользователя-согласующего
        self.APP.g1_api_token.get_token('User2')

        # Получаем id пользователя
        user03_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user3', 'kind': 'Any'})[0]['Id']

        # Добавляем обозревателя
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], add_approver['LastModifiedDate'], [user03_id])

        assert add_observer['Observers'][0]['Id'] == user03_id
        assert add_observer['Approvers'][0]['Id'] == user02_id
        assert add_observer['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']
        assert 'RequestType' in created_request

    @allure.title('Добавление обозревателя (статус "На согласовании")')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_to_request_with_status_on_approval(self):

        # Создание заявки
        created_request = self.g1_create_request()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Добавляем согласующего
        add_approver = self.APP.g1_api_actions_in_request.put_add_approver(created_request['Id'], created_request['LastModifiedDate'], [user02_id])

        # Получаем id пользователя
        user03_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user3', 'kind': 'Any'})[0]['Id']

        # Добавляем обозревателя
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], add_approver['LastModifiedDate'], [user03_id])

        assert add_observer['Observers'][0]['Id'] == user03_id
        assert add_observer['Approvers'][0]['Id'] == user02_id
        assert add_observer['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']
        assert 'RequestType' in created_request

    @allure.title('Добавление обозревателя (статус "В работе")')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_to_request_with_status_on_work(self):

        # Создание заявки
        created_request = self.g1_create_request()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Добавляем обозревателя
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], created_request['LastModifiedDate'], [user02_id])

        assert 'RequestType' in created_request
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']
        assert add_observer['Observers'][0]['Id'] == user02_id

    @allure.title('Добавление обозревателя (исполнитель)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip('Не проходит запрос с добавлением исполнителя 403')
    def test_add_observer_by_contractor(self):

        # Создание заявки
        created_request = self.g1_create_request()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Назначем исполнителя
        self.APP.g1_api_actions_in_request.update_contractor_in_request(created_request['Id'], created_request['LastModifiedDate'], user02_id)

        # Переходим на исполнителя
        self.APP.g1_api_token.get_token('User2')

        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']

        # Добавляем обозревателя
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], created_request['LastModifiedDate'], [user06_id])

        assert add_observer['Observers'][0]['Id'] == user06_id
        assert add_observer['Contractor'][0]['Id'] == user02_id
        assert 'RequestType' in created_request

    @allure.title('Добавление обязательного обозревателя из классификатора')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_by_rg(self):

        # Создание заявки
        created_request = self.g1_create_request({'JobType': 'Тип для тестирования(2)'})

        # Получаем id пользователя
        boss02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test Boss2'})[0]['Id']

        assert created_request['Observers'][0]['Id'] == boss02_id
        assert 'RequestType' in created_request

    @allure.title('403 если пользователя нет в списке обозревателей (группы и т.д.)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_user_not_found_anywhere_in_request(self):

        # Создание заявки
        created_request = self.g1_create_request({'JobType': 'Тип для тестирования(2)'})

        # Переход на пользователя не состоящего где-либо в заявке
        self.APP.g1_api_token.get_token('User5')

        # Получить информацию о заявке
        info_about_request = self.APP.g1_api_requests.get_requests_id(created_request['Id'])

        assert info_about_request.status_code == 403
        assert 'RequestType' in created_request

    @allure.title('Добавление обозревателя (статус "Закрыта")')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip('Не проходит запрос с добавлением исполнителя 403')
    def test_add_observer_to_close_request(self):

        # Создание заявки
        created_request = self.g1_create_request({})

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Назначем исполнителя
        add_contractor = self.APP.g1_api_actions_in_request.update_contractor_in_request(created_request['Id'], created_request['LastModifiedDate'], user02_id)

        # Отправить на проверку
        resolve_request = self.APP.g1_api_actions_in_request.actions_in_request(created_request['Id'], add_contractor['LastModifiedDate'], self.APP.group_data.g1_tickets_actions['RUS']['Отправить на проверку'])

        # Закрыть заявку
        close_request = self.APP.g1_api_actions_in_request.actions_in_request(created_request['Id'], resolve_request['LastModifiedDate'], self.APP.group_data.g1_tickets_actions['RUS']['Оценить и закрыть'], rating=5)

        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']

        # Добавляем обозревателя
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], created_request['LastModifiedDate'], [user06_id])

        assert close_request['Status'] == self.APP.group_data.g1_Status_ticket['RUS']['Закрыта']
        assert add_observer['Observers'][0]['Id'] == user06_id
        assert 'RequestType' in created_request

    @allure.title('Добавление обозревателя (статус "Закрыта")')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_by_operator(self):

        # Создание заявки
        created_request = self.g1_create_request({})

        # Переход на системного оператора
        self.APP.g1_api_token.get_token()

        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        # Добавляем обозревателя
        add_observer = self.APP.g1_api_actions_in_request.update_observers_in_request(created_request['Id'], created_request['LastModifiedDate'], [user02_id])

        assert add_observer['Observers'][0]['Id'] == user02_id
        assert 'RequestType' in created_request
