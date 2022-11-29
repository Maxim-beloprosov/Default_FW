import allure

from fw.api.api_base import APIBase


class ApiAddresses(APIBase):

    @allure.step('Фильтрация по списку элементов. POST /api/Addresses/Filter')
    def post_addresses_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Addresses/Filter', body, params)