import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiKnowledgeBase(G1APIBase):

    @allure.step('Получить данные по ноде. GET api/KnowledgeBase/{id}')
    def get_knowledge_base_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/KnowledgeBase/{id}', params)

    @allure.step('Вернуть все актуальные и те на которые есть разрешения ноды базы знаний. GET api/KnowledgeBase/Nodes')
    def get_knowledge_base_nodes(self, params=None):
        return self.requests_GET(self.get_base_url() + 'api/KnowledgeBase/Nodes', params)

    @allure.step('Создание ноды. Поддерживается в description создание картинки из base64. POST api/KnowledgeBase')
    def post_knowledge_base(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/KnowledgeBase', body, params)

    @allure.step('Удалить ноду. DELETE api/KnowledgeBase/{id}')
    def delete_knowledge_base_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/KnowledgeBase/{id}', params)