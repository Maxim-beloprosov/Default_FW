import allure

from fw.api.api_base import APIBase


class ApiFileManagerFilesBackground(APIBase):


    @allure.step('Создание превью файлов (если их еще нет). POST /api/FilesBackground/RepairMiniatures/Start')
    def post_create_preview_files_if_they_not_exist_yet(self):
        return self.requests_POST(self.get_base_url() + '/api/FilesBackground/RepairMiniatures/Start')

    @allure.step('Остановить cоздание превью файлов. POST /api/FilesBackground/RepairMiniatures/Stop')
    def post_stop_creating_preview_files(self):
        return self.requests_POST(self.get_base_url() + '/api/FilesBackground/RepairMiniatures/Stop')

    @allure.step('Получить информацию о текущем состоянии создания превью файлов. GET /api/FilesBackground/RepairMiniatures/Progress')
    def get_info_about_current_state_creating_preview_files(self):
        return self.requests_GET(self.get_base_url() + '/api/FilesBackground/RepairMiniatures/Progress')
