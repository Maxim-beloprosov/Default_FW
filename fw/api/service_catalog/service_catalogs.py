import allure

from fw.api.api_base import APIBase


class ServiceCatalogs(APIBase):

    @allure.step('Получение каталога услуг по ключу. GET /api/ServiceCatalogs/{id}')
    def get_service_catalogs_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/ServiceCatalogs/{id}', params)

    @allure.step('Обновление каталога услуг. PUT /api/ServiceCatalogs/{id}')
    def put_service_catalogs_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/ServiceCatalogs/{id}', body, params)

    @allure.step('Удаление каталога услуг. DELETE /api/ServiceCatalogs/{id}')
    def delete_service_catalogs_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/ServiceCatalogs/{id}', params)

    @allure.step('Список каталогов услуг по идентификаторам. POST /api/ServiceCatalogs/ListByIds')
    def post_service_catalogs_list_by_ids(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/ListByIds', body, params)

    @allure.step('Создание каталога услуг. POST /api/ServiceCatalogs')
    def post_service_catalogs(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs', body, params)

    @allure.step('Восстановление каталога услуг. PUT /api/ServiceCatalogs/{id}/Restore')
    def put_service_catalogs_id_restore(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/ServiceCatalogs/{id}/Restore', body, params)

    @allure.step('Поиск каталогов услуг с учетом фильтра. Результат: отфильтрованный список каталогов со всеми родителями. POST /api/ServiceCatalogs/FilterTreeList')
    def post_service_catalogs_filter_tree_list(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/FilterTreeList', body, params)

    @allure.step('Поиск каталогов услуг с учетом фильтра. Результат: отфильтрованный список каталогов без родителей и детей (по всему дереву). POST /api/ServiceCatalogs/FilterList')
    def post_service_catalogs_filter_list(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/FilterList', body, params)

    @allure.step('Поиск каталогов услуг с учетом фильтра и по родительскому идентификатору (если он не указан, то только для верхнего уровня). POST /api/ServiceCatalogs/FilterParentTreeList')
    def post_service_catalogs_filter_parent_tree_list(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/FilterParentTreeList', body, params)

    @allure.step('Поиск каталога по идентификатору и фильтру. Результат: родители каталога и все прямые дети этих родителей с учетом пагинации. POST /api/ServiceCatalogs/FilterFullTreeList')
    def post_service_catalogs_filter_full_tree_list(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/FilterFullTreeList', body, params)

    @allure.step('Выполнить массовые операции над каталогами по списку идентификаторов. POST /api/ServiceCatalogs/BulkActionByIds')
    def post_service_catalogs_bulk_action_by_ids(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/BulkActionByIds', body, params)

    @allure.step('Выполнить массовые операции над каталогами по списку идентификаторов. POST /api/ServiceCatalogs/CatalogsAndGandivaServiceCount')
    def post_service_catalogs_and_gandiva_service_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/CatalogsAndGandivaServiceCount', body, params)

    @allure.step('Кол-во элементов каталогов/услуг для заданного фильтра. POST /api/ServiceCatalogs/Filter/CatalogsAndGandivaServiceCount')
    def post_service_catalogs_filter_catalogs_and_gandiva_service_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/Filter/CatalogsAndGandivaServiceCount', body, params)

    @allure.step('Получение кол-ва дочерних элементов с учетом фильтра. POST /api/ServiceCatalogs/Filter/ChildrenCount')
    def post_service_catalogs_filter_children_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/Filter/ChildrenCount', body, params)

    @allure.step('Обновление права доступа для инициаторов. PUT /api/ServiceCatalogs/{id}/Access/Initiators')
    def put_service_catalogs_id_access_initiators(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/ServiceCatalogs/{id}/Access/Initiators', body, params)

    @allure.step('Список доступных инициаторов для обновления права доступа инициаторов. POST /api/ServiceCatalogs/{id}/Access/Initiators/Filter')
    def post_service_catalogs_id_access_initiators_filter(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/{id}/Access/Initiators/Filter', body, params)

    @allure.step('Список доступных инициаторов для установки права доступа инициаторов. POST /api/ServiceCatalogs/Access/Initiators/Filter')
    def post_service_catalogs_access_initiators_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ServiceCatalogs/Access/Initiators/Filter', body, params)

    @allure.step('Получение списка типов возможных прав доступа инициаторов. GET /api/ServiceCatalogs/Actions/InitiatorAccessTypes')
    def get_service_catalogs_actions_initiator_access_types(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/ServiceCatalogs/Actions/InitiatorAccessTypes', params)

    @allure.step('Поиск каталогов услуг с учетом фильтра для создания тикета. POST /api/GandivaServicesForTickets/Filter')
    def post_gandiva_services_for_tickets_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/GandivaServicesForTickets/Filter', body, params)

