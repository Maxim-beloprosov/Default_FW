import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Редактирование задач')
class TestEditTask(G1ApiBase):

    @allure.title('Смена заголовка задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_change_subject_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # Меняем заголовок задачи
        task = self.APP.g1_api_actions_in_task.g1_edit_subject_in_task(task['Id'], task['LastModifiedDate'], 'AutomationApiTest Subject')
        assert task['Subject'] == 'AutomationApiTest Subject'

    @allure.title('Смена даты начала задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_change_begin_date_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        begin_date = self.APP.time.get_date_increased_x_days_json(1)
        # Меняем дату начала в задаче
        task = self.APP.g1_api_actions_in_task.change_task_start_date(task['Id'], task['LastModifiedDate'], begin_date)
        assert task['RequiredStartDate'] == begin_date
        assert task['Status'] == self.APP.group_data.g1_Status_ticket['Task']['RUS']['Ожидает']

    @allure.title('Смена даты окончания задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_change_end_date_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        end_date = self.APP.time.get_date_increased_x_days_json(1)
        # Меняем дату окончания в задаче
        task = self.APP.g1_api_actions_in_task.g1_change_end_date_in_task(task['Id'], task['LastModifiedDate'], end_date)
        assert task['RequiredCompletionDate'] == end_date

    @allure.title('Редактировать описание в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_edit_description_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        description = 'AutomationApiTest EditDescription'
        # Изменяем описание в задаче
        task = self.APP.g1_api_actions_in_task.g1_edit_description_in_task(task['Id'], task['LastModifiedDate'], description)
        assert task['Description'] == description

    @allure.title('Редактировать хэштеги задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_edit_hashtags_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        hashtags = ['automation', 'api', 'test']
        # Редактируем хэтеги в задаче
        task = self.APP.g1_api_actions_in_task.g1_edit_hashtags_in_task(task['Id'], task['LastModifiedDate'], hashtags)
        assert set(task['HashTags']) == set(hashtags)

    @allure.title('Сменить исполнителя в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_change_contractor_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # id нового исполнителя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # Меняем исполнителя в задаче
        task = self.APP.g1_api_actions_in_task.g1_change_contractor_in_task(task['Id'], task['LastModifiedDate'], user02_id)
        assert task['Contractors'][0]['Id'] == user02_id

    @allure.title('Оставить персональный комментарий в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_personal_comment_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # Текст для комментария
        text = 'AutomationApiTest Comment'
        # Адресат комментария
        user = self.APP.g1_api_users.get_users_current()['Id']
        # Добавляем комментарий
        comment = self.APP.g1_api_actions_in_task.g1_add_comment_in_task(task['Id'], text, [user])
        assert comment['Author']['Id'] == user
        assert comment['Addressees'][0]['User']['Id'] == user
        assert comment['Text'] == text

    @allure.title('Оставить комментарий нескольким пользователям в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_comment_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
        # Текст для комментария
        text = 'AutomationApiTest Comment'
        # Адресаты комментария
        users = [self.APP.g1_api_users.get_users_current()['Id'], user01_id]
        # Добавляем комментарий
        comment = self.APP.g1_api_actions_in_task.g1_add_comment_in_task(task['Id'], text, users)
        # Формируем список id всех адресатов
        adressees_id = self.APP.g1_api_actions_in_task.g1_list_all_addreesses_comment_in_task(comment['Addressees'])
        assert comment['Author']['Id'] == users[0]
        assert set(users) == set(adressees_id)
        assert comment['Text'] == text

    @allure.title('Добавление обозревателя в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_observer_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # ид пользователя - обозревателя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # Добавляем обозревателя
        task = self.APP.g1_api_actions_in_task.g1_add_observers_in_task(task['Id'], task['LastModifiedDate'], user02_id)
        assert task['Observers'][0]['Id'] == user02_id
        assert len(task['Observers']) == 1

    @allure.title('Добавление нескольких обозревателей в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_several_observers_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # ид пользователя - обозревателя
        user02_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user2', 'kind': 'Any'})[0]['Id']
        # ид пользователя - обозревателя
        user04_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user4', 'kind': 'Any'})[0]['Id']
        # Добавляем обозревателя
        task = self.APP.g1_api_actions_in_task.g1_add_observers_in_task(task['Id'], task['LastModifiedDate'], [user02_id, user04_id])
        # Формируем список всех id обозревателей
        observers = self.APP.g1_api_actions_in_task.g1_list_all_observers_in_task(task['Observers'])
        assert user02_id in observers
        assert user04_id in observers
        assert len(observers) == 2

    @allure.title('Добавление вложенной заявки в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_subrequest_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # Создаем заявку
        request = self.g1_create_request()
        # Добавляем заявку к задаче в качестве вложенной
        task = self.APP.g1_api_actions_in_task.g1_add_subrequest_in_task(task['Id'], request['Id'], task['LastModifiedDate'])
        assert request['Id'] in task['SubRequests']

    @allure.title('Добавление вложенной задачи в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_add_subtask_in_task(self):
        # Создаем задачу
        task = self.g1_create_task()
        # Создаем  2 задачу
        task_2 = self.g1_create_task()
        # Добавляем заявку к задаче в качестве вложенной
        task = self.APP.g1_api_actions_in_task.g1_add_subtask_in_task(task['Id'], task_2['Id'], task['LastModifiedDate'])
        assert task_2['Id'] in task['SubTasks']



