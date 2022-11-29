import allure

from fw.api.api_base import APIBase


class ApiRequests(APIBase):

    @allure.step('Список заявок. POST /api/Requests/Filter')
    def post_requests_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Requests/Filter', body, params)

    @allure.step('Получение заявки по ключу. GET /api/Requests/{id}')
    def get_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}', params)

    @allure.step('Обновление заявки. PUT /api/Requests/{id}')
    def put_requests_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}', body, params)

    @allure.step('Удалить согласование. DELETE /api/Requests/{id}/Agreements/{agreementId}')
    def delete_requests_id_agreements_agreement_id(self, id, agreementId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Requests/{id}/Agreements/{agreementId}', params)

