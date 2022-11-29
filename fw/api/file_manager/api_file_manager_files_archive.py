import allure

from fw.api.api_base import APIBase


class ApiFileManagerFilesArchive(APIBase):

    pass

    # @allure.step('Нет названия. POST /api/FilesArchive/Archive')
    # def post_undefined(self, body):
    #     return self.requests_POST(self.get_base_url() + '/api/FilesArchive/Archive', body)
    #
    # @allure.step('Нет названия. GET /api/FilesArchive/Archive/{archiveId}/IsReady')
    # def post_undefined(self, archiveId):
    #     return self.requests_GET(self.get_base_url() + f'/api/FilesArchive/Archive/{archiveId}/IsReady')
    #
    # @allure.step('Нет названия. GET /api/FilesArchive/Archive/{archiveId}')
    # def post_undefined(self, archiveId):
    #     return self.requests_GET(self.get_base_url() + f'/api/FilesArchive/Archive/{archiveId}')