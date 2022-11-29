import allure

from fw.api.api_base import APIBase


class ApiAccess(APIBase):

    @allure.step('Обновление прав доступа к статье. PUT /api/KnowledgeBase/Pages/{id}/Access')
    def put_update_access_rights_to_article(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}/Access', body, params)

    @allure.step('Возвращаем права доступа к статье. GET /api/KnowledgeBase/Pages/{id}/Access')
    def put_return_access_rights_to_article(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}/Access', params)

    @allure.step('Поиск, сортировка и фильтрация клиентов для установки прав доступа к статье. POST /api/KnowledgeBase/Pages/AccessMembers/Filter')
    def put_search_sort_filter_clients_for_access_rights_to_article(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages/AccessMembers/Filter', body, params)

    @allure.step('Массовое копирование прав доступа. POST /api/KnowledgeBase/Pages/Access/BulkCopy')
    def put_mass_copy_access_rights(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages/Access/BulkCopy', body, params)