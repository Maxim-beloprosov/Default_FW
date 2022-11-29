import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiAccessSheet(G1APIBase):

    @allure.step('Получение листа допуска. GET api/AccessSheet/{id}')
    def get_access_sheet_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/AccessSheet/{id}', params)

    @allure.step('Создание листа допуска по выбранному списку ресрусов. POST api/AccessSheet')
    def post_access_sheet(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/AccessSheet', body, params)

    @allure.step('Получить список листов допуска с фильтрацией. POST api/AccessSheet/Search')
    def post_access_sheet_search(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/AccessSheet/Search', body, params)
