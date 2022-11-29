import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiPermissions(G1APIBase):

    @allure.step('Разрешения при создании заявки. GET api/Permissions/Request/New')
    def get_permissions_request_new(self, params=None):
        return self.requests_GET(self.get_base_url() + 'api/Permissions/Request/New', params)

    @allure.step('Разрешения при редактировании заявки. GET api/Permissions/Request/Edit/{id}')
    def get_permissions_request_edit_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Permissions/Request/Edit/{id}', params)

    @allure.step('Разрешения при создании задачи. GET api/Permissions/Task/New')
    def get_permissions_task_new(self, params=None):
        return self.requests_GET(self.get_base_url() + 'api/Permissions/Task/New', params)

    @allure.step('Разрешения при редактировании заявки. GET api/Permissions/Task/Edit/{id}')
    def get_permissions_task_edit_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Permissions/Task/Edit/{id}', params)
