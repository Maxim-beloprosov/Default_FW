import allure

from fw.api.api_base import APIBase

class ApiTaskCustomFieldCollection(APIBase):

    @allure.step('Получение дополнительных полей по Id задачи. GET /api/TaskCustomFieldCollection/{id}')
    def get_task_custom_field_collection_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/TaskCustomFieldCollection/{id}', params)

    @allure.step('Обновление дополнительных полей задачи. PUT /api/TaskCustomFieldCollection/{id}')
    def put_task_custom_field_collection_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/TaskCustomFieldCollection/{id}', body, params)