import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiReports(G1APIBase):

    @allure.step('Получение списка отчётов GET api/Reports')
    def get_reports(self, params=None):
        return self.requests_GET(self.get_base_url() + 'api/Reports', params)

    @allure.step('Сформировать указанный отчёт. POST api/Reports/{id}/download')
    def post_reports_id_download(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Reports/{id}/download', body, params)
