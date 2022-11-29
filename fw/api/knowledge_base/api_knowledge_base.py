import allure

from fw.api.api_base import APIBase


class ApiKnowledgeBase(APIBase):

    @allure.step('Создание статьи. POST /api/KnowledgeBase/Pages')
    def post_create_article(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages', body, params)

    @allure.step('Получение статьи по ключу. GET /api/KnowledgeBase/Pages/{id}')
    def get_article_by_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}', params)

    @allure.step('Обновление статьи. PUT /api/KnowledgeBase/Pages/{id}')
    def put_update_article_by_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}', body, params)

    @allure.step('Получение статьи для редактирования. GET /api/KnowledgeBase/Pages/{id}/ToEdit')
    def get_article_for_editing(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}/ToEdit', params)

    @allure.step('Количество доступных пользователю статей. GET /api/KnowledgeBase/Pages/Count')
    def get_count_available_articles_for_user(self, params=None):
        return self.requests_GET(self.get_base_url() + '/api/KnowledgeBase/Pages/Count', params)

    @allure.step('Получение дочерних статей. POST /api/KnowledgeBase/Pages/TreeChildren')
    def post_get_children_articles(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages/TreeChildren', body, params)

    @allure.step('Получений Родителей. POST api/KnowledgeBase/Pages/TreeParent')
    def post_get_parent_articles(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/KnowledgeBase/Pages/TreeParent', body, params)

    @allure.step('Получение списка статей с минимальным набором св-в и усеченным текстом статьи. POST /api/KnowledgeBase/Pages/Short')
    def post_get_articles_with_minimal_params_and_truncated_article_texts(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages/Short', body, params)

    @allure.step('Поиск и фильтрация статей. POST /api/KnowledgeBase/Pages/Filter')
    def post_search_and_filter_articles(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages/Filter', body, params)

    @allure.step('Для каждого идентификатора статьи из списка, возвращаем количество доступных дочерних статей. POST /api/KnowledgeBase/Pages/CountChildren')
    def post_return_available_articles_for_every_identificator_article_in_list(self, body=[], params=None):
        return self.requests_POST(self.get_base_url() + '/api/KnowledgeBase/Pages/CountChildren', body, params)

    @allure.step('Удаление/Восстановление статьи. POST /api/KnowledgeBase/Pages/{id}/DeleteRestore')
    def post_delete_or_restore_article(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}/DeleteRestore', body, params)

    @allure.step('Возврат файла. GET /api/KnowledgeBase/files/{fileId}')
    def post_return_file(self, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/KnowledgeBase/files/{fileId}', params)

    @allure.step('Перемещение статьи. POST /api/KnowledgeBase/Pages/{id}/Move')
    def post_move_article(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/KnowledgeBase/Pages/{id}/Move', body, params)
