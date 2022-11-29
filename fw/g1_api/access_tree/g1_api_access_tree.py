import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiAccessTree(G1APIBase):

    @allure.step('Получить ресурс допуска. GET api/AccessTree/{id}')
    def get_access_tree_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/AccessTree/{id}', params)

    @allure.step('Поуровневое получение дерева ресурсов допуска. GET api/AccessTree/ChildrenNodes/{id}')
    def get_access_tree_children_nodes_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/AccessTree/ChildrenNodes/{id}', params)

    @allure.step('Создание ресурса допуска. POST api/AccessTree')
    def post_access_tree(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/AccessTree', body, params)

    @allure.step('Создание ресурса допуска. POST api/AccessTree/Search')
    def post_access_tree_search(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/AccessTree/Search', body, params)

    @allure.step('Редактирование ресурса допуска. PUT api/AccessTree')
    def put_access_tree(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + 'api/AccessTree', body, params)
