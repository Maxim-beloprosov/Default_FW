import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Общая информация.')
class TestApiSchemasCommon(G1ApiBase):

    @allure.title('GET api/Common/HashTags/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_common_hash_tags_search(self):
        # Ищем хэштэг
        search = self.APP.g1_api_common.get_common_hash_tags_search(params={'text': 'test'})
        assert 'Error' not in search

    @allure.title('GET api/Common/Favourites')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_common_favourites(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Добавляем задачу в избранное
        self.APP.g1_api_tasks.post_tasks_id_favourites(created_task['Id'])
        # Возвращает список избранных элементов для данного пользовател
        favourites = self.APP.g1_api_common.get_common_favourites()[0]
        assert 'Id' in favourites
        assert 'Kind' in favourites
        assert 'Status' in favourites
        assert 'Initiator' in favourites

    @allure.title('GET api/Common/Find')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_common_find(self):
        # Создаём задачу
        created_task = self.g1_create_task()
        # Поиск задачи/заявки по Id
        task_or_request = self.APP.g1_api_common.get_common_find(params={'id': created_task['Id']})
        assert 'Id' in task_or_request[0]
        assert 'Kind' in task_or_request[0]
        assert 'Status' in task_or_request[0]
        assert 'Initiator' in task_or_request[0]

    @allure.title('GET api/Common/ping')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_common_ping(self):
        # Пингуем сервер
        ping = self.APP.g1_api_common.get_common_ping()
        assert ping.status_code == 200

    @allure.title('PUT api/Common/Comments/id/Read')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_common_comments_id_read(self):
        # Создаём задачу
        created_task = self.g1_create_task({})
        # Читаем все комменты
        read_comment = self.APP.g1_api_common.put_common_comments_id_read(created_task['Id'])
        assert 'Id' in read_comment
        assert 'Author' in read_comment
        assert 'JointAuthors' in read_comment
        assert 'Addressees' in read_comment
        assert 'Text' in read_comment

    @allure.title('PUT api/Common/Comments/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_common_comments_id(self):
        # Создаём задачу
        created_task = self.g1_create_task({})
        # Добавляем комментарий
        new_comment = self.APP.g1_api_tasks.post_tasks_id_comments(created_task['Id'], {'Text': 'Тестовый комментарий'})
        # Редактировать комментарий
        edit_comment = self.APP.g1_api_common.put_common_comments_id(new_comment['Id'], {'Text': 'Новый текст комментария'})
        assert 'Id' in edit_comment
        assert 'Author' in edit_comment
        assert 'JointAuthors' in edit_comment
        assert 'Addressees' in edit_comment
        assert edit_comment['Text'] == 'Новый текст комментария'
        assert 'CreateDate' in edit_comment
        assert 'CommentType' in edit_comment
        assert 'Answers' in edit_comment
        assert 'ReadStatus' in edit_comment

    @allure.title('DELETE api/Common/Comments/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Земцов Владислав')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_common_comments_id(self):
        # Создаём задачу
        created_task = self.g1_create_task({})
        # Добавляем комментарий
        new_comment = self.APP.g1_api_tasks.post_tasks_id_comments(created_task['Id'], {'Text': 'Тестовый комментарий'})
        # Удаляем комментарий
        delete_comment = self.APP.g1_api_common.delete_common_comments_id(new_comment['Id'])
        assert 'Target' in delete_comment
        assert delete_comment['Status'] == self.APP.group_data.g1_result_status['RUS']['Успех']
        assert 'Error' in delete_comment
