import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка создания заявки')
class Test_request_api(G1ApiBase):

    """
    4) Создание заявки (дополнительные поля, заполнение)
    6) Создание заявки (изменение классификатора)
    """

    @allure.title('Создание заявки (ГО без диспетчера)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_without_dispatcher(self):
        # Создаем заявку
        created_request = self.g1_create_request({})
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']
        assert created_request['Contractor'] == None

    @allure.title('Создание заявки (инициатор выбирает исполнителя из группы')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_with_choice_contractor(self):
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # Создаем заявку
        created_request = self.g1_create_request({'Contractor': {'Id': user02_id}})
        assert created_request['Contractor']['Id'] == user02_id
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Создание заявки (есть обязательный согласующий, обязательный обозреватель)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_with_obligatory_approver_and_observer(self):
        # Новый норматив
        normative_type = 'Тип для тестирования(2)'
        # Создаем заявку
        created_request = self.g1_create_request({'JobType': normative_type})
        # Получаем id пользователя
        boss01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test Boss1', 'kind': 'Any'})[0]['Id']
        # Получаем id пользователя
        boss02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test Boss2', 'kind': 'Any'})[0]['Id']
        assert created_request['Department']['Name'] == self.APP.group_data.service_template_g1[normative_type]['department']
        assert created_request['Category']['Name'] == self.APP.group_data.service_template_g1[normative_type]['category']
        assert created_request['RequestType']['Name'] == self.APP.group_data.service_template_g1[normative_type]['type']
        assert created_request['JobType']['Name'] == self.APP.group_data.service_template_g1[normative_type]['job_type']
        assert created_request['Approvers'][0]['Id'] == boss01_id
        assert created_request['Observers'][0]['Id'] == boss02_id
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['На согласовании']

    @allure.title('Создание заявки (добавление обозревателя)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_with_observer_1(self):
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # Создание заявки
        created_request = self.g1_create_request({'Observers': {"IsUserAdded": True, "Id": user02_id}})
        assert created_request['Observers'][0]['Id'] == user02_id
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']

    @allure.title('Создание заявки (Проверка региона)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_with_check_region(self):
        # Создание заявки
        created_request = self.g1_create_request({})
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']
        assert created_request['Region']['Name'] == '-'

    @allure.title('Создание заявки (Проверка региона, изменение региона до создания)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_with_new_region(self):
        new_region = 'Нижний Новгород'
        # Создание заявки
        created_request = self.g1_create_request({'Region': new_region})
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']
        assert created_request['Region']['Name'] == new_region

    @allure.title('Создание заявки (всплывающее окно)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_with_pop_up_window(self):
        # Создание заявки
        created_request = self.g1_create_request({})
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['В работе']
        assert created_request['NormativeNote'] == ''
        #TODO Добавить примечание в норматив, когда будет метод изменения норматива

    @allure.title('Создание заявки (Дата рассмотрения)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_create_request_through_classifier(self):
        # Создание заявки
        created_request = self.g1_create_request({'RequiredStartDate': 1})
        assert created_request['Status'] == self.APP.group_data.g1_Status_ticket['Request']['RUS']['Ожидает']

