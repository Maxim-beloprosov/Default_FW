import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiUsers(G1APIBase):

    @allure.step('Возвращает фото пользователя по идентификатору. GET api/Users/{Id}/photo')
    def get_users_id_photo(self, Id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/{Id}/photo', params)

    @allure.step('Возвращает фото текущего пользователя. GET api/Users/photo')
    def get_users_photo(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/photo', params)

    @allure.step('Профиль пользователя с идентификатором id. GET api/Users/{id}')
    def get_users_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/{id}', params)

    @allure.step('Профиль пользователя. GET api/Users/profile')
    def get_users_profile(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/profile', params)

    @allure.step('Профиль текущего пользователя. GET api/Users/current')
    def get_users_current(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/current', params)

    @allure.step('Осуществляет поиск сотрудников. GET api/Users/search')
    def get_users_search(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/search', params=params)

    @allure.step('Принадлежность текущего пользователя группам ответственности(не системным). GET api/Users/ResponsibilityGroups')
    def get_users_responsibility_groups(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/ResponsibilityGroups', params)

    @allure.step('Список всех регионов. GET api/Users/Regions')
    def get_users_regions(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Users/Regions', params)

    @allure.step('Загрузить фото пользователя. POST api/Users/photo')
    def post_users_photo(self, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Users/photo', params)

    @allure.step('Получить рабочую загруженность списка пользователей. POST api/Users/FunctioningCapacity')
    def post_users_function_capacity(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Users/FunctioningCapacity', body, params)

    @allure.step('Редактировать профиль текущего пользователя. PUT api/Users/current')
    def put_users_current(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Users/current', body, params)

    @allure.step('Редактировать профиль пользователя по Id. PUT api/Users')
    def put_users(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Users', body, params)

    @allure.step('Передать активные согласования одного пользователя другому. PUT api/Users/{id}/MoveActiveAgrimentsToUser/{target}?setAlternate={setAlternate}')
    def put_transfer_active_approvals_from_one_user_to_another(self, id, target, setAlternate, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Users/{id}/MoveActiveAgrimentsToUser/{target}?setAlternate={setAlternate}', params)
