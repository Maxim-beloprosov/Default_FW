import allure

from fw.api.api_base import APIBase


class ResponsibilityGroups(APIBase):

    @allure.step('Получение Группы ответственности по ключу. GET /api/ResponsibilityGroups/{id}')
    def get_responsibility_groups_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/ResponsibilityGroups/{id}', params)

    @allure.step('Обновление группы ответственности. PUT /api/ResponsibilityGroups/{id}')
    def put_responsibility_groups_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/ResponsibilityGroups/{id}', body, params)

    @allure.step('Создание группы ответственноси. POST /api/ResponsibilityGroups')
    def post_responsibility_groups(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/ResponsibilityGroups', body, params)

    @allure.step('Получение элементов дерева "Групп ответственности". POST /api/ResponsibilityGroups/Tree')
    def post_responsibility_groups_tree(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/ResponsibilityGroups/Tree', body, params)

    @allure.step('Поиск и фильтрация в коллекции "Групп ответственности". POST /api/ResponsibilityGroups/Filter')
    def post_responsibility_groups_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/ResponsibilityGroups/Filter', body, params)

    @allure.step('Поиск и фильтрация пользователей в "Группа ответственности". POST /api/ResponsibilityGroups/{id}/Users/Filter')
    def post_responsibility_groups_id_users_filter(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ResponsibilityGroups/{id}/Users/Filter', body, params)

    @allure.step('Добавление пользователей в "Группу ответственности". POST /api/ResponsibilityGroups/{id}/Users')
    def post_responsibility_groups_id_users(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/ResponsibilityGroups/{id}/Users', body, params)

    @allure.step('Удаление пользователей из "Группы ответственности". DELETE /api/ResponsibilityGroups/{id}/Users')
    def delete_responsibility_groups_id_users(self, id, body, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/ResponsibilityGroups/{id}/Users', body, params)