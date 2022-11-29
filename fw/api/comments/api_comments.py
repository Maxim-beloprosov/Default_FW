import allure

from fw.api.api_base import APIBase


class ApiComments(APIBase):

    @allure.step('Создание комментария. POST /api/Comments')
    def post_comments(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Comments', body, params)

    @allure.step('Редактирование обычного (пользовательского) комментария. PUT /api/Comments/{id}')
    def put_comments_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Comments/{id}', body, params)

    @allure.step('Удаление комментария. Комментарий не удаляется физически, вместо текста вставляется код: Пользователь userName удалил комментарий. DELETE /api/Comments/{id}')
    def delete_comments_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Comments/{id}', params)

    @allure.step('Прочитать комментарий. POST /api/Comments/{id}/Read.')
    def post_comments_id_read(self, id, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Comments/{id}/Read', params)

    @allure.step('Лента активности, возвращает список не прочитанных комментариев. POST /api/Comments/ActivityTape')
    def post_comments_activity_tape(self, body,params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Comments/ActivityTape', body, params)

    @allure.step('Прочитать все комментарии. POST /api/Comments/Read/All')
    def post_comments_read_all(self, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Comments/Read/All', params)

    @allure.step('Список комментариев. GET /api/Comments')
    def get_comments(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Comments', params)