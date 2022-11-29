import allure

from fw.api.api_base import APIBase


class ApiPositions(APIBase):

    @allure.step('Фильтрация по списку элементов. POST /api/Positions/Filter')
    def post_positions_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Positions/Filter', body, params)
