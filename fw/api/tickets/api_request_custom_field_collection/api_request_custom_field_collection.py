import allure

from fw.api.api_base import APIBase


class ApiRequestCustomFieldCollection(APIBase):

    @allure.step('Получение дополнительных полей по id заявки. GET /api/Request/CustomFieldCollection/{id}')
    def get_request_custom_field_collection_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/RequestCustomFieldCollection/{id}', params)

    @allure.step('Обновление значений дополнительных полей заявки. PUT /api/RequestCustomFieldCollection/{id}')
    def put_request_custom_field_collection_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/RequestCustomFieldCollection/{id}', body, params)