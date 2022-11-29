import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Заявки.')
class TestApiSchemasRequest(G1ApiBase):

    @allure.title('GET api/requests')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_requests(self):
        request = self.APP.g1_api_requests.get_api_requests(params={'type': 'forgroup', 'page': 1, 'size': 20, 'sort': 'Department'})
        assert self.APP.group_data.response.status_code == 200
        assert 'Requests' in request
        assert 'Total' in request
        assert request['Page'] == 1
        assert request['PageSize'] == 20

    @allure.title('GET api/Requests/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id(self):
        # Создаем заявку
        request = self.g1_create_request()
        request = self.APP.g1_api_requests.get_requests_id(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request

    @allure.title('GET api/Requests/id/RequestResponsibilityGroupUsers')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_request_responsibility_group_users(self):
        # Создаем заявку
        request = self.g1_create_request()
        request = self.APP.g1_api_requests.get_requests_id_request_responsibility_group_users(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'FirstName' in request[0]
        assert 'LastName' in request[0]

    @allure.title('GET api/Requests/id/GetContractorsList')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_get_contractors_list(self):
        request = self.g1_create_request()
        request = self.APP.g1_api_requests.get_requests_id_get_contractors_list(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'FirstName' in request[0]
        assert 'LastName' in request[0]

    @allure.title('POST api/Requests/Filter')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_filter(self):
        body = {
            'Filtering': {'Departments': [38]},
            'BaseFilter': 0,
            'Page': 1,
            'Size': 20,
            'Sorting': 0,
            'Descending': False
        }
        request = self.APP.g1_api_requests.post_requests_filter(body)

        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Total' in request
        assert request['Page'] == 1
        assert request['PageSize'] == 20
        assert 'Requests' in request

    @allure.title('POST api/Requests/FilterCount')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_filter_count(self):
        body = {
            'Filtering': {'Departments': [38]},
            'BaseFilter': 0,
            'Page': 1,
            'Size': 20,
            'Sorting': 0,
            'Descending': False
        }
        request = self.APP.g1_api_requests.post_requests_filter_count(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int

    @allure.title('POST api/Requests/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_search(self):
        body = {
            'SearchString': 'Отдел тестирования Гандивы',
            'Page': 1,
            'Size': 20,
            'Sorting': 0,
            'Descending': False
        }
        request = self.APP.g1_api_requests.post_requests_search(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Total' in request
        assert request['Page'] == 1
        assert request['PageSize'] == 20
        assert 'Requests' in request

    @allure.title('POST api/Requests/SearchCount')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_search_count(self):
        body = {
            'SearchString': 'Отдел тестирования Гандивы',
            'Page': 1,
            'Size': 20,
            'Sorting': 0,
            'Descending': False
        }

        request = self.APP.g1_api_requests.post_requests_search_count(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert type(request) == int

    @allure.title('POST api/Requests')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests(self):
        request = self.g1_create_request()
        assert request
        assert self.APP.group_data.response.status_code == 201
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request

    @allure.title('GET api/Requests/id/Copy')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_copy_mask(self):
        request = self.g1_create_request()
        request = self.APP.g1_api_requests.get_requests_id_copy_mask(request['Id'], 1)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request

    @allure.title('POST api/Requests/id/Favourites')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_id_favourites(self):
        request = self.g1_create_request()
        request = self.APP.g1_api_requests.post_requests_id_favorites(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Target' in request
        assert 'Status' in request
        assert 'Error' in request

    @allure.title('DELETE api/Requests/id/Favourites')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_requests_id_favourites(self):
        request = self.g1_create_request()
        self.APP.g1_api_requests.post_requests_id_favorites(request['Id'])
        request = self.APP.g1_api_requests.delete_requests_id_favourites(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Target' in request
        assert 'Status' in request
        assert 'Error' in request

    @allure.title('PUT api/Requests/id/Observers')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_observers(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Observers': [{'Id': user02_id}]
        }
        request = self.APP.g1_api_requests.put_requests_id_observers(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request

    @allure.title('POST api/Requests/id/Comments')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_id_comments(self):
        #Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # Добавление обозревателя в заявку.
        self.APP.g1_api_actions_in_request.update_observers_in_request(request['Id'], request['LastModifiedDate'], [user02_id])
        # пишем коммент
        request = self.APP.g1_api_requests.post_requests_id_comments(request['Id'], body={'Text': 'AutomationApiTest Comment', 'Addressees': [1]})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Author' in request
        assert 'Addressees' in request
        assert request['Text'] == 'AutomationApiTest Comment'

    @allure.title('PUT api/Requests/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id(self):
        # Создаем заявку
        request = self.g1_create_request()
        request['Description'] = 'AutomationApiTest Descriptions'
        # редактируем заявку
        request = self.APP.g1_api_requests.put_requests_id(request['Id'], body=request)
        assert request
        assert request['Description'] == 'AutomationApiTest Descriptions'
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request

    @allure.title('GET api/Requests/id/Comments')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_comments(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # Добавление обозревателя в заявку.
        self.APP.g1_api_actions_in_request.update_observers_in_request(request['Id'], request['LastModifiedDate'], [user02_id])
        # пишем коммент
        self.APP.g1_api_requests.post_requests_id_comments(request['Id'], body={'Text': 'AutomationApiTest Comment', 'Addressees': [1]})
        # получаем комментарии заявки
        request = self.APP.g1_api_requests.get_requests_id_comments(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'Author' in request[0]
        assert 'Addressees' in request[0]
        assert 'CreateDate' in request[0]
        assert 'CommentType' in request[0]

    @allure.title('PUT api/Requests/id/Contractor')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_contractor(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # устанавливаем исполнителя
        request = self.APP.g1_api_requests.put_requests_id_contractor(request['Id'], body={'LastModifiedDate': request['LastModifiedDate'], 'Contractor': {'Id': user01_id}})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request

    @allure.title('PUT api/Requests/id/SubRequests/subRequestId')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_subrequests_subrequests_id(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Contractor': {'Id': user02_id}
        }
        # устанавливаем исполнителя
        request = self.APP.g1_api_requests.put_requests_id_contractor(request['Id'], body)
        request_two = self.g1_create_request()

        params = {'lastModifiedDate': request['LastModifiedDate']}
        request = self.APP.g1_api_requests.put_requests_id_subrequests_subrequests_id(request['Id'], request_two['Id'], params=params)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert request['SubRequests'][0] == int(request_two['Id'])

    @allure.title('GET api/Requests/id/SubRequests')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_sub_requests(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Contractor': {'Id': user01_id}
        }
        # устанавливаем исполнителя
        request = self.APP.g1_api_requests.put_requests_id_contractor(request['Id'], body)
        request_two = self.g1_create_request()
        self.APP.g1_api_requests.put_requests_id_subrequests_subrequests_id(request['Id'], request_two['Id'], request['LastModifiedDate'])

        request = self.APP.g1_api_requests.get_requests_id_sub_requests(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Total' in request
        assert 'Page' in request
        assert 'PageSize' in request
        assert 'Requests' in request

    @allure.title('GET api/Requests/id/DependentRequests')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_dependent_requests(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        body = {'LastModifiedDate': request['LastModifiedDate'], 'Contractor': {'Id': user01_id}}
        # устанавливаем исполнителя
        request = self.APP.g1_api_requests.put_requests_id_contractor(request['Id'], body)
        request_two = self.g1_create_request()
        self.APP.g1_api_requests.put_requests_id_subrequests_subrequests_id(request['Id'], request_two['Id'], params={'lastModifiedDate': request['LastModifiedDate']})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        request = self.APP.g1_api_requests.get_requests_id_dependent_requests(request_two['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Total' in request
        assert 'Page' in request
        assert 'PageSize' in request
        assert 'Requests' in request

    @allure.title('POST api/Requests/UserFilter')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_user_filter(self):
        request = self.APP.g1_api_requests.post_requests_user_filter(body={'Filter': {'Departments': [38]}, 'Name': 'AutomationTestFilter' + self.APP.time.get_time_now()})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Target' in request
        assert 'Status' in request
        assert 'Error' in request

    @allure.title('GET api/Requests/UserFilters')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_user_filters(self):
        body = {
            'Filter': {'Departments': [38]},
            'Name': 'AutomationTestFilter' + self.APP.time.get_time_now()
        }
        self.APP.g1_api_requests.post_requests_user_filter(body)
        request = self.APP.g1_api_requests.get_requests_user_filters()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Filter' in request[0]
        assert 'Id' in request[0]
        assert 'Name' in request[0]

    @allure.title('POST api/Requests/FilterByStatusOnPeriod')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_filter_by_status_on_period(self):
        body = {
            'Filtering': {'Departments': [38]},
            'Page': 1,
            'Size': 20,
            'Sorting': 0,
            'Descending': False
        }
        request = self.APP.g1_api_requests.post_requests_filter_by_status_on_period(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Total' in request
        assert request['Page'] == 1
        assert request['PageSize'] == 20
        assert 'Requests' in request

    @allure.title('POST api/Requests/Recalculated')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_recalculated(self):
        # Создаем заявку
        request = self.g1_create_request()
        request = self.APP.g1_api_requests.post_requests_recalculated(request)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request

    @allure.title('GET api/Requests/id/DependentTasks')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_requests_id_dependent_tasks(self):
        # Создаем заявку
        request = self.g1_create_request()
        #Создаем задачу
        task = self.g1_create_task()
        # Привязываем заявку к задаче
        self.APP.g1_api_tasks.put_tasks_id_sub_requests_request_id(task['Id'], request['Id'], params={'LastModifiedDate': task['LastModifiedDate']})
        # Получаем список задач, к которым привязана заявка
        request = self.APP.g1_api_requests.get_requests_id_dependent_tasks(request['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Total' in request
        assert 'Page' in request
        assert 'PageSize' in request
        assert 'Tasks' in request

    @allure.title('PUT api/Requests/v2/id/Approvers')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_approvers(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Approvers': [
                {
                    'Id': 0,
                    'UserId': user02_id,
                    'Status': 0,
                    'IsUserAdded': True
                }
            ]
        }
        # Добавляем согласующего
        request = self.APP.g1_api_requests.put_requests_id_approvers(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert 'Initiator' in request
        assert request['Approvers'][0]['Id'] == user02_id

    @allure.title('POST api/Requests/id/ClarificationQuestion')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_id_clarification_question(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Approvers': [
                {
                    'Id': 0,
                    'UserId': user02_id,
                    'Status': 0,
                    'IsUserAdded': True
                }]}
        # Добавляем согласующего
        request = self.APP.g1_api_requests.put_requests_id_approvers(request['Id'], body)

        # Перелогиниваемся на согласующего
        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')

        body = {'ClarificationType': 0, 'Text': 'AutomationApiTest ClarificationQuestion'}
        # Задаем вопрос-уточнение
        request = self.APP.g1_api_requests.post_requests_id_clarification_question(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'LastModifiedDate' in request
        assert 'RequestStatus' in request
        assert 'Comment' in request

    @allure.title('POST api/Requests/Comments/id/ClarificationAnswer')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_comments_id_clarification_answer(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']

        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Approvers': [
                {
                    'Id': 0,
                    'UserId': user02_id,
                    'Status': 0,
                    'IsUserAdded': True
                }
            ]
        }
        # Добавляем согласующего
        request = self.APP.g1_api_requests.put_requests_id_approvers(request['Id'], body)
        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')

        body = {'ClarificationType': 0, 'Text': 'AutomationApiTest ClarificationQuestion'}
        # Задаем вопрос-уточнение
        request = self.APP.g1_api_requests.post_requests_id_clarification_question(request['Id'], body)

        # Перелогиниваемся обратно на инициатора
        self.APP.g1_api_token.get_token()
        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        # Отвечаем на вопрос-уточнение
        request = self.APP.g1_api_requests.post_requests_comments_id_clarification_answer(request['Comment']['Id'], body={'Text': 'AutomationApiTest ClarificationAnswer'})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'LastModifiedDate' in request
        assert 'RequestStatus' in request
        assert 'Comment' in request

    @allure.title('POST api/Requests/Comments/id/Join')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_comments_id_join(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id 1 пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']
        # Получаем id 2 пользователя
        user04_id = self.APP.g1_api_users.get_users_search(params={'text': 'Владислав Земцов', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Approvers': [
                {
                    'Id': 0,
                    'UserId': user02_id,
                    'Status': 0,
                    'IsUserAdded': True
                },
                {
                    'Id': 0,
                    'UserId': user04_id,
                    'Status': 0,
                    'IsUserAdded': True
                }
            ]
        }

        # Добавляем согласующего
        request = self.APP.g1_api_requests.put_requests_id_approvers(request['Id'], body)
        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')
        # Задаем вопрос-уточнение
        request = self.APP.g1_api_requests.post_requests_id_clarification_question(request['Id'], body={'ClarificationType': 0, 'Text': 'AutomationApiTest ClarificationQuestion'})

        # Перелогиниваемся на 2 согласующего
        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token(login='agat\\v.zemtsov', password='Subwoofer100123077')

        # Присоединяемся к вопросу-уточнению
        request = self.APP.g1_api_requests.post_requests_comments_id_join(request['Comment']['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Addressees' in request
        assert 'Text' in request
        assert 'CreateDate' in request
        assert 'CommentType' in request

    @allure.title('PUT api/Requests/Comments/id/Join')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_comments_id_join(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id 1 пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']
        # Получаем id 2 пользователя
        user04_id = self.APP.g1_api_users.get_users_search(params={'text': 'Владислав Земцов', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Approvers':
                [
                    {
                        'Id': 0,
                        'UserId': user02_id,
                        'Status': 0,
                        'IsUserAdded': True
                    },
                    {
                        'Id': 0,
                        'UserId': user04_id,
                        'Status': 0,
                        'IsUserAdded': True
                    }
                ]
        }
        # Добавляем согласующего
        request = self.APP.g1_api_requests.put_requests_id_approvers(request['Id'], body)
        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')

        # Задаем вопрос-уточнение
        body = {'ClarificationType': 0, 'Text': 'AutomationApiTest ClarificationQuestion'}
        request = self.APP.g1_api_requests.post_requests_id_clarification_question(request['Id'], body)
        # Перелогиниваемся на 2 согласующего
        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token(login='agat\\v.zemtsov', password='Subwoofer100123077')

        # Присоединяемся к вопросу-уточнению
        request = self.APP.g1_api_requests.put_requests_comments_id_join(request['Comment']['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Addressees' in request
        assert 'Text' in request
        assert 'CreateDate' in request
        assert 'CommentType' in request

    @allure.title('POST api/Requests/Comments/id/CancelClarification')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_comments_id_cancel_clarification(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id 1 пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Approvers': [
                {
                    'Id': 0,
                    'UserId': user02_id,
                    'Status': 0,
                    'IsUserAdded': True
                }
            ]
        }
        # Добавляем согласующего
        request = self.APP.g1_api_requests.put_requests_id_approvers(request['Id'], body)
        # Перелогиниваемся на согласующего
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')

        # Задаем вопрос-уточнение
        body = {'ClarificationType': 0, 'Text': 'AutomationApiTest ClarificationQuestion'}
        request = self.APP.g1_api_requests.post_requests_id_clarification_question(request['Id'], body)

        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')
        # Отменяем вопрос-уточнение
        request = self.APP.g1_api_requests.post_requests_comments_id_cancel_clarification(request['Comment']['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Target' in request
        assert 'Status' in request
        assert 'Error' in request

    @allure.title('PUT api/Requests/id/Path')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_path(self):
        # Создаем заявку
        request = self.g1_create_request()

        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'DepartmentId': 38,
            'CategoryId': 489,
            'RequestTypeId': 2552,
            'JobTypeId': 13731,
            'RequestCustomFields': []
        }
        # Обновляем заявку
        request = self.APP.g1_api_requests.put_requests_id_path(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert 'Initiator' in request

    @allure.title('PUT api/Requests/id/Initiator')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_initiator(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        body = {'LastModifiedDate': request['LastModifiedDate'], 'Person': {'Id': user02_id}}
        # Обновляем инициатора
        request = self.APP.g1_api_requests.put_requests_id_initiator(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert request['Initiator']['Id'] == user02_id

    @allure.title('DELETE api/Requests/id/SubRequests/subRequestId')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_requests_id_subrequests__subrequests_id(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']

        body = {
            'LastModifiedDate': request['LastModifiedDate'],
            'Contractor': {'Id': user02_id}
        }
        # устанавливаем исполнителя
        request = self.APP.g1_api_requests.put_requests_id_contractor(request['Id'], body)
        # Создаем вторую заявку
        request_two = self.g1_create_request()
        # Привязываем вторую заявку к 1
        self.APP.g1_api_requests.put_requests_id_subrequests_subrequests_id(request['Id'], request_two['Id'], request['LastModifiedDate'])

        # Удаляем у заявки вложенную заявку
        params = {'lastModifiedDate': request['LastModifiedDate']}
        request = self.APP.g1_api_requests.delete_requests_id_subrequests__subrequests_id(request['Id'], request_two['Id'], params=params)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert request['SubRequests'] == []

    @allure.title('PUT api/Requests/id/Hashtags')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_hashtags(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Обновляем заявку
        request = self.APP.g1_api_requests.put_requests_id_hashtags(request['Id'], body={'LastModifiedDate': request['LastModifiedDate'], 'HashTags': ['automation']})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert request['HashTags'][0] == 'automation'

    @allure.title('PUT api/Requests/id/Region')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_region(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Обновляем заявку
        request = self.APP.g1_api_requests.put_requests_id_region(request['Id'], body={'LastModifiedDate': request['LastModifiedDate'], 'Region': {'Id': 1}})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert request['Region']['Id'] == 1

    @allure.title('PUT api/Requests/id/Action')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_action(self):
        # Создаем заявку
        request = self.g1_create_request()

        body = {'LastModifiedDate': request['LastModifiedDate'], 'BidAction': 8, 'Description': 'AutomationApiTest Cancel'}
        # Меняем статус заявки на "Отменена"
        request = self.APP.g1_api_requests.put_requests_id_action(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request
        assert request['Status'] == 7

    @allure.title('PUT api/Requests/id/RequiredStartDate')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_required_start_date(self):
        # Создаем заявку
        request = self.g1_create_request()

        body = {'LastModifiedDate': request['LastModifiedDate'], 'RequiredStartDate': request['LastModifiedDate']}
        # Обновляем дату
        request = self.APP.g1_api_requests.put_requests_id_required_start_date(request['Id'], body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request
        assert 'Status' in request
        assert 'Department' in request
        assert 'Category' in request
        assert 'RequestType' in request
        assert 'JobType' in request
        assert 'Description' in request

    @allure.title('PUT api/Requests/id/ReadAll')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_requests_id_read_all(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Получаем id пользователя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'Антон Кустов', 'kind': 'Any'})[0]['Id']
        # Добавление обозревателя в заявку.
        self.APP.g1_api_actions_in_request.update_observers_in_request(request['Id'], request['LastModifiedDate'], [user02_id])
        # Перелогиниваемся на обозревателя
        self.APP.g1_api_token.get_token(login='agat\\a.kustov', password='Hitmanqw12')
        # пишем коммент
        self.APP.g1_api_requests.post_requests_id_comments(request['Id'], body={'Text': 'AutomationApiTest Comment', 'Addressees': [user02_id]})
        # перелогиниваемся на инициатора
        self.APP.g1_api_token.get_token()
        # Читаем комменты
        request = self.APP.g1_api_requests.put_requests_id_read_all(request['Id'])
        assert request
        assert request.status_code == 200

    @allure.title('POST api/Requests/RequestsByIdList')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_requests_requests_by_id_list(self):
        # Создаем заявку
        request = self.g1_create_request()
        # получаем заявки
        request = self.APP.g1_api_requests.post_requests_requests_by_id_list(body=[request['Id']])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'Status' in request[0]
        assert 'Department' in request[0]
        assert 'Category' in request[0]
        assert 'RequestType' in request[0]
        assert 'JobType' in request[0]
        assert 'Description' in request[0]
