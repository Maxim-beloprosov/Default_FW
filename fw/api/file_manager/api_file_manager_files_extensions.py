import allure

from fw.api.api_base import APIBase


class ApiFileManagerFilesExtensions(APIBase):

    @allure.step('Получение списка допустимых базовых типов файлов. GET /api/FilesExtensions/MimeTypes')
    def post_get_list_allowed_base_file_types(self):
        return self.requests_GET(self.get_base_url() + '/api/FilesExtensions/MimeTypes')

    @allure.step('Получение списка известных расширений файлов. GET /api/FilesExtensions/FileTypeExtension')
    def get_list_known_file_extensions(self):
        return self.requests_GET(self.get_base_url() + '/api/FilesExtensions/FileTypeExtension')

    @allure.step('Получение MimeType файла по его полному имени (должно быть указано расширение файла). GET /api/FilesExtensions/MimeTypes/{fileName}')
    def get_mime_type_file_by_full_name(self, fileName):
        return self.requests_GET(self.get_base_url() + f'/api/FilesExtensions/MimeTypes/{fileName}')
