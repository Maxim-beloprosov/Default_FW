import allure

from fw.api.api_base import APIBase


class ApiFileManagerFiles(APIBase):

    @allure.step('Загрузка файлов на сервер. POST /api/Files/Upload')
    def post_upload_files_to_server(self, file_path):
        return self.upload_file(file_path, self.get_base_url() + '/api/Files/Upload')

    @allure.step('Получение информации о файле по его идентификатору. GET /api/Files/{id}/Info')
    def get_info_about_file_by_id(self, id):
        return self.requests_GET(self.get_base_url() + f'/api/Files/{id}/Info')

    @allure.step('Получение файла с сервера по идентификатору. GET /api/Files/{id}')
    def get_file_from_server_by_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Files/{id}', params)

    @allure.step('Удаление файла с сервера по идентификатору. DELETE /api/Files/{id}')
    def delete_file_from_server_by_id(self, id):
        return self.requests_DELETE(self.get_base_url() + f'/api/Files/{id}')

    @allure.step('Обновление имени файла на сервере по идентификатору. PUT /api/Files/{id}')
    def put_update_file_name_on_server_by_id(self, id, file_name):
        return self.requests_PUT(self.get_base_url() + f'/api/Files/{id}', None, file_name)
