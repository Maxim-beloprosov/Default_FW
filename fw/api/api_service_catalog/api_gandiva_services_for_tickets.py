import allure

from fw.api.api_base import APIBase


class ApiGandivaServicesForTickets(APIBase):

    @allure.step('Получение услуги по ключу для создания заявки или ресурса допуска. GET /api/GandivaServicesForTickets/{id}')
    def get_gandiva_services_for_tickets_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/GandivaServicesForTickets/{id}', params)

    @allure.step('Получение каталога услуг по ключу для создания заявки или ресурса допуска. GET /api/GandivaServicesForTickets/Catalog/{id}')
    def get_gandiva_services_for_tickets_catalog_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/GandivaServicesForTickets/Catalog/{id}', params)

    @allure.step('Поиск каталогов услуг с учетом фильтра для создания тикета. POST /api/GandivaServicesForTickets/Filter')
    def post_gandiva_services_for_tickets_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/GandivaServicesForTickets/Filter', body, params)

    @allure.step('Получение кол-ва дочерних элементов с учетом фильтра . POST /api/GandivaServicesForTickets/Filter/ChildrenCount')
    def post_gandiva_services_for_tickets_filter_children_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/GandivaServicesForTickets/Filter/ChildrenCount', body, params)




