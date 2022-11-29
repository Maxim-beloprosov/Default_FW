import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiTaskUserFilters(G1APIBase):

    @allure.step('Получить все фильтры задач пользователя. GET api/TaskUserFilters')
    def get_task_user_filters(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/TaskUserFilters', params)

    @allure.step('Добавляет новый пользовательский фильтр. POST api/TaskUserFilters')
    def post_task_user_filters(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/TaskUserFilters', body, params)

    @allure.step('Редактировать пользовательский фильтр. PUT api/TaskUserFilters/{id}')
    def put_task_user_filters_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/TaskUserFilters/{id}', body, params)

    @allure.step('Удалить пользовательский фильтр. DELETE api/TaskUserFilters/{id}')
    def delete_task_user_filters_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/TaskUserFilters/{id}', params)

    @allure.step('Переименование пользовательского фильтра. PUT api/TaskUserFilters/RenameName/{id}')
    def put_task_user_filters_rename_name_id(self, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/TaskUserFilters/RenameName/{id}', None, params)
