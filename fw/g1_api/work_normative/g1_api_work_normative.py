import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiWorkNormative(G1APIBase):

    @allure.step('Возвращает только активные подразделения. GET api/workNormative/departments')
    def get_work_normative_departments(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/departments', params)

    @allure.step('Отдел норматива с идентификатором Id. GET api/workNormative/departments/{id}')
    def get_work_normative_departments_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/departments/{id}', params)

    @allure.step('Cписок активных категорий для заданного отдела. GET api/workNormative/departments/{department_id}/categories')
    def get_work_normative_departments_department_id_categories(self, department_id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/departments/{department_id}/categories', params)

    @allure.step('Категория с идентификатором Id. GET api/workNormative/categories/{id}')
    def get_work_normative_categories_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/categories/{id}', params)

    @allure.step('Список активных типов заявки для заданной категории. GET api/workNormative/categories/{category_id}/requestTypes')
    def get_work_normative_categories_category_id_request_types(self, category_id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/categories/{category_id}/requestTypes', params)

    @allure.step('Тип заявки с идентификатором Id. GET api/workNormative/requestTypes/{id}')
    def get_work_normative_request_types_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/requestTypes/{id}', params)

    @allure.step('Список активных видов работ для заданного типа заявки. GET api/workNormative/requestTypes/{request_type_id}/jobTypes')
    def get_work_normative_request_types_request_type_id_job_types(self, request_type_id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/requestTypes/{request_type_id}/jobTypes', params)

    @allure.step('Вид работ с идентификатором Id. GET api/workNormative/jobTypes/{id}')
    def get_work_normative_job_types_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/jobTypes/{id}', params)

    @allure.step('Дополнительные поля норматива. GET api/workNormative/CustomFields')
    def get_work_normative_custom_fields(self, params=None):
        """
        departmentId={departmentId}&
        categoryId={categoryId}&
        requestTypeId={requestTypeId}&
        jobTypeId={jobTypeId}&
        requestId={requestId}
        """
        return self.requests_GET(self.get_base_url() + f'api/workNormative/CustomFields', params)

    @allure.step('Дополнительные поля норматива. GET api/workNormative/{id}/CustomFields')
    def get_work_normative_id_custom_fields(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/{id}/CustomFields', params)

    @allure.step('Справочник(список возможных значений) дополнительного поля. GET api/workNormative/CustomFields/{id}/Dictionary')
    def get_work_normative_custom_fields_id_dictionary(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/CustomFields/{id}/Dictionary', params)

    @allure.step('Справочник(список возможных значений) дополнительного поля. GET api/workNormative/{id}/ResponsibilityUsers')
    def get_work_normative_id_responsibility_users(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/{id}/ResponsibilityUsers', params)

    @allure.step('Список пользователей из группы ответственности для норматива. POST api/workNormative/ResponsibilityUsers')
    def post_work_normative_responsibility_users(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/workNormative/ResponsibilityUsers', body, params)

    @allure.step('Поиск нормативов с учетом словоформ искомой фразы. GET api/workNormative/Search')
    def get_work_normative_search(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/Search', params)

    @allure.step('Поиск в нормативах. POST api/workNormative/Search')
    def post_work_normative_search(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/workNormative/Search', body, params)

    @allure.step('Список групп ответственности с входящими в них пользователями. GET api/workNormative/{id}/ResponsibilityGroups')
    def get_work_normative_id_responsibility_groups(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/workNormative/{id}/ResponsibilityGroups', params)

    @allure.step('Список групп ответственности с входящими в них пользователями. POST api/workNormative/ResponsibilityGroups')
    def post_api_work_normative_responsibility_groups(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/workNormative/ResponsibilityGroups', body, params)