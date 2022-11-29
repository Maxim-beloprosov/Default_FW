import allure

from fw.api.api_base import APIBase


class ApiCustomFieldDirectory(APIBase):

    @allure.step('Создание пользовательского справочника. POST /api/CustomFieldDictionary')
    def post_custom_field_dictionary(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/CustomFieldDictionary', body, params)

    @allure.step('Обновление пользовательского справочника. PUT /api/CustomFieldDictionary/{id}')
    def put_custom_field_dictionary(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/CustomFieldDictionary/{id}', body, params)

    @allure.step('Удаление справочника. DELETE /api/CustomFieldDictionary/{id}')
    def delete_custom_field_dictionary(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/CustomFieldDictionary/{id}', params)

    @allure.step('Получение справочника по ключу. GET /api/CustomFieldDictionary/{id}')
    def get_custom_field_dictionary(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/CustomFieldDictionary/{id}', params)

    @allure.step('Восстановление справочника. PUT /api/CustomFieldDictionary/{id}/Restore')
    def put_custom_field_dictionary_restore(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/Restore', body, params)

    @allure.step('Обновление строк в пользовательском справочнике. POST /api/CustomFieldDictionary/{id}/UpdateRows')
    def post_update_field_dictionary(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/UpdateRows', body, params)

    @allure.step('Значения справочников по идентификаторам справочников и идентификаторам строк.'
                 'POST /api/CustomFieldDictionary/Values')
    def post_values_with_lines_field_dictionary(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/CustomFieldDictionary/Values', body, params)

    @allure.step('Значение справочника по идентификатору справочника и идентификатору строки.'
                 'POST /api/CustomFieldDictionary/{id}/Values')
    def post_values_with_line_field_dictionary(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/Values', body, params)

    @allure.step('Поиск справочников с учетом фильтра POST /api/CustomFieldDictionary/Filter')
    def post_search_custom_field_dictionary(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/CustomFieldDictionary/Filter', body, params)

    @allure.step('Поиск значений справочника с учетом фильтра. POST /api/CustomFieldDictionary/{id}/Filter')
    def post_search_values_of_custom_field_dictionary(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/Filter', body, params)

    @allure.step('Получение файла по идентификатору поля и строке. POST /api/CustomFieldDictionary/{id}/File')
    def post_get_file_custom_field_dictionary(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/File', body, params)

    @allure.step('Получение файла по идентификатору поля. GET /api/CustomFieldDictionary/{id}/File')
    def get_file_custom_field_dictionary(self, id, body, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/File', body, params)

    @allure.step('Получение миниатюры файла по идентификатору поля. GET /api/CustomFieldDictionary/{id}/FileMiniature')
    def get_file_miniature_custom_field_dictionary(self, id, body, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/CustomFieldDictionary/{id}/FileMiniature', body, params)











