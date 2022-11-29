import allure

from fw.api.api_base import APIBase


class ApiWorkLoad(APIBase):

    @allure.step('Мониторинг загруженности по ГО. POST /api/WorkLoad/ResponsibilityGroups')
    def post_work_load_responsibility_groups(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/WorkLoad/ResponsibilityGroups', body, params)

    @allure.step('Мониторинг загруженности по задачам. POST /api/WorkLoad/Tasks')
    def post_work_load_tasks(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/WorkLoad/Tasks', body, params)

