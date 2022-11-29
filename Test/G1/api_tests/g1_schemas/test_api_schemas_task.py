import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Задачи.')
class TestApiSchemasTask(G1ApiBase):

    @allure.title('GET api/Tasks')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks(self):
        # Получаем список задач
        tasks = self.APP.g1_api_tasks.get_tasks(params={'type': 'all', 'page': 1, 'size': 20, 'sort': 'Id'})
        assert 'Total' in tasks
        assert tasks['Page'] == 1
        assert tasks['PageSize'] == 20
        assert 'Tasks' in tasks
        assert 'Folders' in tasks

    @allure.title('GET api/Tasks/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Получаем задачу по Id
        task = self.APP.g1_api_tasks.get_tasks_id(created_task['Id'])
        assert task
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in task
        assert 'Status' in task
        assert 'Subject' in task

    @allure.title('GET api/Tasks/id/comments')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id_comments(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Оставляем комментарий
        self.APP.g1_api_tasks.post_tasks_id_comments(created_task['Id'], {'Text': 'TestApiComment' + self.APP.time.get_date_time_Y_m_d_H_M_S()})
        # Получаем список комментариев
        comment = self.APP.g1_api_tasks.get_tasks_id_comments(created_task['Id'])[0]
        assert 'Id' in comment
        assert 'Author' in comment
        assert 'JointAuthors' in comment

    @allure.title('GET api/Tasks/id/SubRequests')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id_sub_requests(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Создаём заявку
        created_request = self.g1_create_request()
        # Добавляем заявку в задачу
        self.APP.g1_api_tasks.put_tasks_id_sub_requests_request_id(created_task['Id'], created_request['Id'], params={'lastModifiedDate': created_task['LastModifiedDate']})
        # Получаем список вложенных заявок
        requests_list = self.APP.g1_api_tasks.get_tasks_id_sub_requests(created_task['Id'])
        assert 'Total' in requests_list
        assert 'Page' in requests_list
        assert 'PageSize' in requests_list
        assert 'Requests' in requests_list

    @allure.title('GET api/Tasks/id/SubTasks')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id_sub_tasks(self):
        # Создаём задачу
        created_task01 = self.g1_create_task()
        # Создаём задачу
        created_task02 = self.g1_create_task()
        # Добавляет зависимую задачу02 в задачу01
        self.APP.g1_api_tasks.put_tasks_id_sub_task_id(created_task01['Id'], created_task02['Id'], params={'lastModifiedDate': created_task01['LastModifiedDate']})
        # Получаем список вложенных задач
        tasks_list = self.APP.g1_api_tasks.get_tasks_id_sub_tasks(created_task01['Id'])
        assert 'Total' in tasks_list
        assert 'Page' in tasks_list
        assert 'PageSize' in tasks_list
        assert 'Tasks' in tasks_list

    @allure.title('GET api/Tasks/id/DependentTasks')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id_dependent_tasks(self):
        # Создаём задачу
        created_task01 = self.g1_create_task()
        # Создаём задачу
        created_task02 = self.g1_create_task()
        # Добавляет зависимую задачу02 в задачу01
        self.APP.g1_api_tasks.put_tasks_id_sub_task_id(created_task01['Id'], created_task02['Id'], params={'lastModifiedDate': created_task01['LastModifiedDate']})
        # Список зависимых задач
        tasks_list = self.APP.g1_api_tasks.get_tasks_id_dependent_tasks(created_task02['Id'])
        assert 'Total' in tasks_list
        assert 'Page' in tasks_list
        assert 'PageSize' in tasks_list
        assert 'Tasks' in tasks_list

    @allure.title('GET api/Tasks/id/SearchAvailableContractors')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id_search_available_contractors(self):
        # Создаём задачу
        created_task01 = self.g1_create_task()
        # Поиск сотрудников для делегирования исполнения
        contractors_list = self.APP.g1_api_tasks.get_tasks_id_search_available_contractors(created_task01['Id'], params={'text': ''})
        assert 'Error' not in contractors_list

    @allure.title('POST api/Tasks/Filter')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_filter(self):
        # Фильтруем задачи
        filter = self.APP.g1_api_tasks.post_tasks_filter({'Page': 1, 'Size': 20})
        assert 'Total' in filter
        assert filter['Page'] == 1
        assert filter['PageSize'] == 20
        assert 'Tasks' in filter
        assert 'Folders' in filter

    @allure.title('POST api/Tasks/FilterCount')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_filter_count(self):
        # Фильтруем задачи
        filter = self.APP.g1_api_tasks.post_tasks_filter_count({})
        assert filter >= 0

    @allure.title('POST api/Tasks/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_search(self):
        # Поиск задач
        search = self.APP.g1_api_tasks.post_tasks_search({'SearchString': 'test', 'Page': 1, 'Size': 20})
        assert 'Total' in search
        assert search['Page'] == 1
        assert search['PageSize'] == 20
        assert 'Tasks' in search

    @allure.title('POST api/Tasks/SearchCount')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_search_count(self):
        # Поиск задач
        search = self.APP.g1_api_tasks.post_tasks_search_count({'SearchString': 'test'})
        assert search >= 0

    @allure.title('POST api/Tasks')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks(self):
        # Создаём задачу
        created_task = self.g1_create_task({})
        assert 'Id' in created_task
        assert 'Contractors' in created_task
        assert 'NewContractor' in created_task

    @allure.title('POST api/Tasks/v3/CreateMultipleTasks')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_v3_create_multiple_tasks(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']
        # Создание списка(множества) новых задач
        task_list = self.APP.g1_api_tasks.post_tasks_v3_create_multiple_tasks({'ContractorIds': [user06_id], 'Task': created_task})
        assert 'TotalCount' in task_list
        assert 'Data' in task_list

    @allure.title('GET api/Tasks/id/Copy')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_tasks_id_copy(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Копируем задачу
        copy_task = self.APP.g1_api_tasks.get_tasks_id_copy(created_task['Id'], params={'mask': self.APP.group_data.g1_copy_mask['Task']['RUS']['Норматив']})
        assert 'Id' in copy_task
        assert 'Contractors' in copy_task

    @allure.title('POST api/Tasks/id/Favourites')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_id_favourites(self):
        # Создаём задачу
        created_task = self.g1_create_task({})
        # Добавляем задачу в избранное
        favourites = self.APP.g1_api_tasks.post_tasks_id_favourites(created_task['Id'])
        assert 'Target' in favourites
        assert favourites['Status'] == self.APP.group_data.g1_result_status['RUS']['Успех']
        assert 'Error' in favourites

    @allure.title('PUT api/Tasks/id/SubRequests/request_id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_sub_requests_request_id(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Создаём заявку
        created_request = self.g1_create_request()
        # Добавляем заявку в задачу
        task = self.APP.g1_api_tasks.put_tasks_id_sub_requests_request_id(created_task['Id'], created_request['Id'],
                                                                          params={'lastModifiedDate': created_task['LastModifiedDate']})
        assert 'Id' in task
        assert 'Contractors' in task

    @allure.title('PUT api/Tasks/id/SubTasks/sub_task_id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_sub_tasks_sub_task_id(self):
        # Создаём задачу
        created_task01 = self.g1_create_task()
        # Создаём задачу
        created_task02 = self.g1_create_task()
        # Добавляет зависимую задачу02 в задачу01
        task = self.APP.g1_api_tasks.put_tasks_id_sub_task_id(created_task01['Id'], created_task02['Id'],
                                                              params={'lastModifiedDate': created_task01['LastModifiedDate']})
        assert 'Id' in task
        assert 'Contractors' in task

    @allure.title('POST api/Tasks/id/Comments')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_api_tasks_id_comments(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Оставляем комментарий
        add_comment = self.APP.g1_api_tasks.post_tasks_id_comments(created_task['Id'], {'Text': 'TestApiComment' + self.APP.time.get_date_time_Y_m_d_H_M_S()})
        assert 'Id' in add_comment
        assert 'Author' in add_comment

    @allure.title('PUT api/Tasks/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Редактирование задачи
        temp = created_task
        temp['Description'] = 'Тест редактирования задачи'
        task = self.APP.g1_api_tasks.put_tasks_id(created_task['Id'], temp)
        assert 'Id' in task
        assert 'Contractors' in task
        assert 'NewContractor' in task

    @allure.title('PUT api/Tasks/id/Observers')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_observers(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': created_task['LastModifiedDate'],
            'Observers':
                [
                    {
                        "IsUserAdded": True,
                        "Id": user06_id
                    }
                ]
        }
        # Добавляем обозревателя
        add_observer = self.APP.g1_api_tasks.put_tasks_id_observers(created_task['Id'], body)
        assert 'Id' in add_observer
        assert 'Contractors' in add_observer
        assert 'NewContractor' in add_observer

    @allure.title('PUT api/Tasks/id/Approvers')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_approvers(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']
        body = {
            'LastModifiedDate': created_task['LastModifiedDate'],
            'Approvers':
                [
                    {
                        "IsUserAdded": True,
                        "Id": user06_id
                    }
                ]
        }

        # Добавляем согласующего
        add_approver = self.APP.g1_api_tasks.put_tasks_id_approvers(created_task['Id'], body)
        assert 'Id' in add_approver
        assert 'Contractors' in add_approver
        assert 'NewContractor' in add_approver

    @allure.title('PUT api/Tasks/id/Hashtags')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_hashtags(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Добавляем хэштег
        hashtag = self.APP.g1_api_tasks.put_tasks_id_hashtags(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'HashTags': ['test']})
        assert 'Id' in hashtag
        assert 'Contractors' in hashtag
        assert 'NewContractor' in hashtag
        assert hashtag['HashTags'][0] == 'test'

    @allure.title('PUT api/Tasks/id/Contractor')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_contractor(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']

        body = {
            'LastModifiedDate': created_task['LastModifiedDate'],
            'Contractor': {"Id": user06_id}
        }

        # Устанавливаем исполнителя
        add_contractor = self.APP.g1_api_tasks.put_tasks_id_contractor(created_task['Id'], body)
        assert 'Id' in add_contractor
        assert add_contractor['Contractors'][0]['Id'] == user06_id
        assert 'NewContractor' in add_contractor
        assert 'Attachments' in add_contractor

    @allure.title('PUT api/Tasks/id/Initiator')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_initiator(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Получаем id пользователя
        user06_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user6', 'kind': 'Any'})[0]['Id']
        # Переходим на пользователя-администратора
        self.APP.g1_api_token.get_token()
        # Изменяем инициатора
        change_initiator = self.APP.g1_api_tasks.put_tasks_id_initiator(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'Person': {'Id': user06_id}})
        assert 'Id' in change_initiator
        assert 'Contractors' in change_initiator
        assert 'NewContractor' in change_initiator
        assert 'Attachments' in change_initiator

    @allure.title('PUT api/Tasks/id/TodoList')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_todo_list(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Добавляем todo_list
        todo = self.APP.g1_api_tasks.put_tasks_id_todo_list(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'ToDoList': [{'Note': 'Test'}]})
        assert 'Id' in todo
        assert 'Contractors' in todo
        assert 'NewContractor' in todo

    @allure.title('PUT api/Tasks/id/Priority')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_priority(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Задаём приоритет
        priority = self.APP.g1_api_tasks.put_tasks_id_priority(created_task['Id'], 1)
        assert 'Target' in priority
        assert priority['Status'] == self.APP.group_data.g1_result_status['RUS']['Успех']
        assert 'Error' in priority

    @allure.title('PUT api/Tasks/id/RequiredDate')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_required_date(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Меняем даты
        change_date = self.APP.g1_api_tasks.put_tasks_id_required_date(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'StartDate': created_task['CreateDate']})
        assert 'Id' in change_date
        assert 'Contractors' in change_date
        assert 'NewContractor' in change_date

    @allure.title('PUT api/Tasks/id/Subject')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_subject(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Редактируем тему
        change_subject = self.APP.g1_api_tasks.put_tasks_id_subject(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'Subject': 'Тестовая тема'})
        assert 'Id' in change_subject
        assert 'Contractors' in change_subject
        assert 'NewContractor' in change_subject

    @allure.title('PUT api/Tasks/id/Description')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_description(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Меняем описание
        change_desc = self.APP.g1_api_tasks.put_tasks_id_description(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'Description': 'Тестовое описание'})
        assert 'Id' in change_desc
        assert 'Contractors' in change_desc
        assert 'NewContractor' in change_desc
        assert 'Attachments' in change_desc
        assert 'Approvers' in change_desc

    @allure.title('PUT api/Tasks/id/Action')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_action(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Отправляем на проверку
        resolve = self.APP.g1_api_tasks.put_tasks_id_action(created_task['Id'], {'LastModifiedDate': created_task['LastModifiedDate'], 'BidAction': self.APP.group_data.g1_tickets_actions['RUS']['Отправить на проверку']})
        assert 'Id' in resolve
        assert 'Contractors' in resolve
        assert 'NewContractor' in resolve
        assert 'Attachments' in resolve

    @allure.title('PUT api/Tasks/id/ReadAll')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_tasks_id_read_all(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Прочитать все комментарии задачи, адресованные текущему пользователю
        read_all = self.APP.g1_api_tasks.put_tasks_id_read_all(created_task['Id'])
        assert 'Target' in read_all
        assert read_all['Status'] == self.APP.group_data.g1_result_status['RUS']['Успех']
        assert 'Error' in read_all

    @allure.title('DELETE api/Tasks/id/Favourites')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_api_tasks_id_favourites(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Добавляем задачу в избранное
        self.APP.g1_api_tasks.post_tasks_id_favourites(created_task['Id'])
        # Удаляем задачу из избранного
        delete_favourites = self.APP.g1_api_tasks.delete_tasks_id_favourites(created_task['Id'])
        assert 'Target' in delete_favourites
        assert delete_favourites['Status'] == self.APP.group_data.g1_result_status['RUS']['Успех']
        assert 'Error' in delete_favourites

    @allure.title('DELETE api/Tasks/id/SubRequests/requestId')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_api_tasks_id_sub_requests_request_id(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Создаём заявку
        created_request = self.g1_create_request()
        # Добавляем заявку в задачу
        task = self.APP.g1_api_tasks.put_tasks_id_sub_requests_request_id(created_task['Id'], created_request['Id'], params={'lastModifiedDate': created_task['LastModifiedDate']})
        # Удаляет заявку из задачи
        delete_request = self.APP.g1_api_tasks.delete_tasks_id_sub_requests_request_id(created_task['Id'], created_request['Id'], params={'lastModifiedDate': task['LastModifiedDate']})
        assert 'Id' in delete_request
        assert 'Contractors' in delete_request
        assert 'NewContractor' in delete_request

    @allure.title('DELETE api/Tasks/id/SubTasks/subTaskId')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_api_tasks_id_sub_tasks_sub_task_id(self):
        # Создаём задачу
        created_task01 = self.g1_create_task()
        # Создаём задачу
        created_task02 = self.g1_create_task()
        # Добавляет зависимую задачу02 в задачу01
        task = self.APP.g1_api_tasks.put_tasks_id_sub_task_id(created_task01['Id'], created_task02['Id'], params={'lastModifiedDate': created_task01['LastModifiedDate']})
        # Удаляем задачу из задачи
        delete_task = self.APP.g1_api_tasks.delete_tasks_id_sub_tasks_sub_task_id(created_task01['Id'], created_task02['Id'], params={'lastModifiedDate': task['LastModifiedDate']})
        assert 'Id' in delete_task
        assert 'Contractors' in delete_task
        assert 'NewContractor' in delete_task
        assert 'Attachments' in delete_task
