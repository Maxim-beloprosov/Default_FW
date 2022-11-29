import allure

from fw.api.api_base import APIBase


class ApiDepartments(APIBase):

    @allure.step('Фильтрация по списку элементов. POST /api/Departments/Filter')
    def post_departments_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Departments/Filter', body, params)
