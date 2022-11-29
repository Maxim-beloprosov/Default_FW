import allure

from fw.api.api_base import APIBase


class ApiFileManagerFilesList(APIBase):

    @allure.step('Получение списка файлов с учетом фильтра. POST /api/FilesList/Filter')
    def post_files_list_filter(self, body):
        return self.requests_POST(self.get_base_url() + '/api/FilesList/Filter', body)

    @allure.step('Получение кол-ва файлов с учетом фильтра. POST /api/FilesList/FilterCount')
    def post_count_files_with_accounting_filter(self, body):
        return self.requests_POST(self.get_base_url() + '/api/FilesList/FilterCount', body)

    @allure.step('Получение архива с файлами по списку идентификаторов. POST /api/FilesList/AsZip')
    def post_get_archive_with_files_by_list_id(self, body):
        return self.requests_POST(self.get_base_url() + '/api/FilesList/AsZip', body)