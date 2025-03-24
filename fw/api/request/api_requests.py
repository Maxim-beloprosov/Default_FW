import allure

from fw.api.api_base import APIBase


class ApiRequests(APIBase):

    @allure.step('Тест POST')
    def post_test(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/test', body, params)

    @allure.step('Тест GET')
    def get_test(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/test/{id}', params)

    @allure.step('Тест PUT')
    def put_test(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/test/{id}', body, params)

    @allure.step('Тест DELETE')
    def delete_test(self, id, test_id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/test/{id}/Agreements/{test_id}', params)

