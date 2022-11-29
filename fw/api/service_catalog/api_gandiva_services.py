import allure

from fw.api.api_base import APIBase


class ApiGandivaServices(APIBase):

    @allure.step('Получение услуги по ключу. GET /api/GandivaServices/{id}')
    def get_gandiva_services_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/GandivaServices/{id}', params)

    @allure.step('Создание услуги. POST /api/GandivaServices')
    def post_gandiva_services(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServices', body, params)

    @allure.step('Обновление услуги. PUT /api/GandivaServices/{id}')
    def put_gandiva_services_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/GandivaServices/{id}', body, params)

    @allure.step('Удаление услуги. DELETE /api/GandivaServices/{id}')
    def delete_gandiva_services_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/GandivaServices/{id}', params)

    @allure.step('Восстановление услуги. PUT /api/GandivaServices/{id}/Restore')
    def put_gandiva_services_id_restore(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/GandivaServices/{id}/Restore', body, params)

    @allure.step('Выполнить массовые операции над услугами по списку идентификаторов. POST /api/GandivaServices/BulkActionByIds')
    def post_gandiva_services_bulk_action_by_ids(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServices/BulkActionByIds', body, params)

    @allure.step('Выполнить массовые операции над услугами по фильтру. POST /api/GandivaServices/BulkActionByFilter')
    def post_gandiva_services_bulk_action_by_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServices/BulkActionByFilter', body, params)

    @allure.step('Остановить массовые операции. POST /api/GandivaServices/StopBulkActions')
    def post_gandiva_services_stop_bulk_actions(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServices/StopBulkActions', body, params)

    @allure.step('Получить информацию о текущем состоянии массовых операций. GET /api/GandivaServices/ProgressBulkActions')
    def get_gandiva_services_progress_bulk_actions(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/GandivaServices/ProgressBulkActions', params)

    @allure.step('Обновление права доступа для инициаторов. PUT /api/GandivaServices/{id}/Access/Initiators')
    def put_gandiva_services_id_access_initiators(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/GandivaServices/{id}/Access/Initiators', body, params)

    @allure.step('Список доступных инициаторов для обновления права доступа инициаторов. POST /api/GandivaServices/{id}/Access/Initiators/Filter')
    def post_gandiva_services_id_access_initiators_filter(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServices/{id}/Access/Initiators/Filter', body, params)

    @allure.step('Список доступных инициаторов для установки права доступа инициаторов. POST /api/GandivaServices/Access/Initiators/Filter')
    def post_gandiva_services_access_initiators_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServices/Access/Initiators/Filter', body, params)

    @allure.step('Получение списка типов возможных прав доступа инициаторов. GET /api/GandivaServices/Actions/InitiatorAccessTypes')
    def get_gandiva_services_actions_initiator_access_types(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/GandivaServices/Actions/InitiatorAccessTypes', params)
