import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiCustomFields(G1APIBase):

    @allure.step('Поиск типов микросправочника с постраничным выводом, с учетом сортировки и фильтрации. POST api/CustomFields/SearchType')
    def post_custom_fields_search_type(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/CustomFields/SearchType', body, params)

    @allure.step('Поиск элементов микросправочника с постраничным выводом, с учетом сортировки и фильтрации. POST api/CustomFields/Search')
    def post_custom_fields_search(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/CustomFields/Search', body, params)

    @allure.step('Создать элемент микросправочника. POST api/CustomFields')
    def post_custom_fields(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/CustomFields', body, params)

    @allure.step('Создать микросправочник. POST api/CustomFields/Type')
    def post_custom_fields_type(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/CustomFields/Type', body, params)

    @allure.step('Редактирование элемента микросправочника с идентификатором id. PUT api/CustomFields/{id}')
    def put_custom_fields_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/CustomFields/{id}', body, params)

    @allure.step('Изменить актуальность элемента микросправочника с номером id. POST api/CustomFields/{id}')
    def post_custom_fields_id_is_actual(self, id, params=None):
        return self.requests_POST(self.get_base_url() + f'api/CustomFields/{id}', None, params)