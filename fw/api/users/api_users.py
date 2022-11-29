import allure

from fw.api.api_base import APIBase


class ApiUsers(APIBase):

    @allure.step('Поиск и фильтрация по пользователям. POST /api/Users/Filter')
    def post_users_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Users/Filter', body, params)

    @allure.step('Количество найденных элементов. POST /api/Users/Filter/Count')
    def post_users_filter_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Users/Filter/Count', body, params)

    @allure.step('Поиск и фильтрация по пользователям. POST /api/Users/Filter/ShortInfo')
    def post_users_filter_short_info(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Users/Filter/ShortInfo', body, params)

    @allure.step('Поиск и фильтрация по пользователям. POST /api/Users/Filter/DetailInfo')
    def post_users_filter_detail_info(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Users/Filter/DetailInfo', body, params)

    @allure.step('Получение пользователя по ключу. GET /api/Users/{id}')
    def get_users_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}', params)

    @allure.step('Обновление пользователя. PUT /api/Users/{id}')
    def put_users_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Users/{id}', body, params)

    @allure.step('Получение сокращенной информации о пользователе по ключу. GET /api/Users/{id}/Short')
    def get_users_id_short(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}/Short', params)

    @allure.step('Получение полного профиля пользователя по ключу. GET /api/Users/{id}/Detail')
    def get_users_id_detail(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}/Detail', params)

    @allure.step('Создание пользователя. POST /api/Users')
    def post_users(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users', body, params)

    @allure.step('Получение информации о всех ключах пользователя. GET /api/Users/Secrets')
    def get_users_secrets(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/Secrets', params)

    @allure.step('Получение информации о всех ключах пользователей. POST /api/Users/Secrets/Filter')
    def post_users_secrets_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users/Secrets/Filter', body, params)

    @allure.step('Получение информации о всех ключах пользователя. GET /api/Users/{user_id}/Secrets')
    def get_users_user_id_secrets(self, user_id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{user_id}/Secrets', params)

    @allure.step('Получение информации об определенном ключе пользователя. GET /api/Users/{user_id}/Secrets/{secret_id}')
    def get_users_user_id_secrets_secret_id(self, user_id, secret_id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{user_id}/Secrets/{secret_id}', params)

    @allure.step('Регенерация ключа пользователя. POST /api/Users/{user_id}/Secrets/{secret_id}')
    def post_users_user_id_secrets_secret_id(self, user_id, secret_id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users/{user_id}/Secrets/{secret_id}', body, params)

    @allure.step('Обновление информации ключа ( например, продление срока действия). PUT /api/Users/{user_id}/Secrets/{secret_id}')
    def put_users_user_id_secrets_secret_id(self, user_id, secret_id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Users/{user_id}/Secrets/{secret_id}', body, params)

    @allure.step('Генерация ключа пользователя. POST /api/Users/{user_id}/Secrets')
    def post_users_user_id_secrets(self, user_id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users/{user_id}/Secrets', body, params)

    @allure.step('Изменить статус аккаунта пользователя. PUT /api/Users/{user_id}/ChangeStatus')
    def put_users_id_change_status(self, user_id, body=None, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Users/{user_id}/ChangeStatus', body, params=params)

    @allure.step('Удаление ключа пользователя. DELETE /api/Users/{userId}/Secrets/{secretId}')
    def delete_users_users_id_secrets_secret_id(self, userId, secretId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Users/{userId}/Secrets/{secretId}', params)

    @allure.step('Получение своего пользовательского профиля. GET /api/Users/Profile')
    def get_users_profile(self, params=None):
        return self.requests_GET(self.get_base_url() + '/api/Users/Profile', params)

    @allure.step('Получение списка своих подчиненных. GET /api/Users/Profile/Subordinate')
    def get_users_profile_subordinate(self, params=None):
        return self.requests_GET(self.get_base_url() + '/api/Users/Profile/Subordinate', params)

    @allure.step('Получение полного профиля пользователя по логину. GET /api/Users/{login}/Profile')
    def get_users_login_profile(self, login, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{login}/Profile', params)

    @allure.step('Получение полного профиля пользователя по идентификатору. GET /api/Users/{userId}/Profile')
    def get_users_user_id_profile(self, userId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{userId}/Profile', params)

    @allure.step('Получение настроек пользователя. GET /api/Users/{id}/Settings')
    def get_users_id_settings(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}/Settings', params)

    @allure.step('Обновление настроек пользователя. PUT /api/Users/{id}/Settings')
    def put_users_id_settings(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Users/{id}/Settings', body, params)

    @allure.step('Список пользователей по идентификаторам. POST /api/Users/ListByIds')
    def post_users_list_by_ids(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users/ListByIds', body, params)

    @allure.step('Получение списка подчиненных. GET /api/Users/{id}/Subordinate')
    def get_users_id_subordinate(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}/Subordinate', params)

    @allure.step('Массовое обновление пользователей. PUT /api/Users/Bulk')
    def put_users_bulk(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + '/api/Users/Bulk', body, params)

    @allure.step('Массовое обновление справочника по шаблону. PUT /api/Users/Bulk/Template')
    def put_users_bulk_template(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + '/api/Users/Bulk/Template', body, params)

    @allure.step('Получить шаблон excel файла для импорта пользователей. GET /api/Users/Import/TemplateExcel')
    def get_users_import_template_excel(self, params=None):
        return self.requests_GET(self.get_base_url() + '/api/Users/Import/TemplateExcel', params)

    @allure.step('Импорт пользователей из excel файла во временную таблицу сервера. POST /api/Users/Import/TemplateExcel/Upload')
    def post_users_import_template_excel_upload(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Users/Import/TemplateExcel/Upload', body, params)

    @allure.step('Запустить импортирование данных из временной таблицы с данными в микросервис. '
                 'Примечание: перед импортом необходимо загрузить заполненный excel файл шаблона на сервер. POST /api/Users/Import/Start')
    def post_users_import_start(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Users/Import/Start', body, params)

    @allure.step('Прогресс публикаций после импорта пользователей/данных. GET /api/Users/Import/Progress')
    def get_users_import_progress(self, params=None):
        return self.requests_GET(self.get_base_url() + '/api/Users/Import/Progress', params)

    @allure.step('Получение аватара пользователя с сервера. GET /api/Users/{id}/Avatar')
    def get_users_id_avatar(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}/Avatar', params)

    @allure.step('Загрузка аватара пользователя на сервер. POST /api/Users/{id}/Avatar')
    def post_users_id_avatar(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users/{id}/Avatar', body, params)

    @allure.step('Удаление аватара с сервера по идентификатору пользователя. DELETE /api/Users/{id}/Avatar')
    def delete_users_id_avatar(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Users/{id}/Avatar', params)

    @allure.step('Получение миниатюры аватара с сервера по идентификатору. GET /api/Users/{id}/AvatarMiniature')
    def get_users_id_avatar_miniature(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Users/{id}/AvatarMiniature', params)

    @allure.step('Загрузка аватара пользователя на сервер по логину. POST /api/Users/{login}/AvatarByLogin')
    def post_users_login_avatar_by_login(self, login, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Users/{login}/AvatarByLogin', body, params)