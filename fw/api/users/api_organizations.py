import allure

from fw.api.api_base import APIBase


class ApiOrganizations(APIBase):

    @allure.step('Фильтрация по списку элементов. POST /api/Organizations/Filter')
    def post_organizations_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Organizations/Filter', body, params)
