import allure

from fw.api.api_base import APIBase


class ApiFileManagerFilesImage(APIBase):

    @allure.step('Получение миниатюры изображения по идентификатору изображения. GET /api/FilesImage/{id}/Miniature')
    def get_miniature_by_id_image(self, id):
        return self.requests_GET(self.get_base_url() + f'/api/FilesImage/{id}/Miniature')

    @allure.step('Получение файла с сервера по идентификатору в формате base64. GET /api/FilesImage/{id}/AsBase64')
    def get_file_from_server_by_id_in_format_base64(self, id):
        return self.requests_GET(self.get_base_url() + f'/api/FilesImage/{id}/AsBase64')

    @allure.step('Загрузка файла на сервер в формате base64. POST /api/FilesImage/UploadBase64')
    def post_upload_file_to_server_in_format_base64(self, body):
        return self.requests_POST(self.get_base_url() + '/api/FilesImage/UploadBase64', body)

    # @allure.step('Получить миниатюру изображения без сохранения на сервер. POST /api/FilesImage/ResizeByHeight')
    # def post_get_miniature_image_without_save_on_server(self, height, body):
    #     return self.requests_POST(self.get_base_url() + f'/api/FilesImage/ResizeByHeight', height, body)