import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Работа с отчетами')
class TestApiSchemasReports(G1ApiBase):

    @allure.title('GET api/Reports')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/21358', name='API. G1. /api/Reports')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip(reason='Метод не работает.')
    def test_get_api_reports(self):
        # Получаем отчеты
        request = self.APP.g1_api_reports.get_reports()
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Items' in request

    @allure.title('POST api/Reports/id/download')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/21361', name='API. G1. api/Reports/id/download')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    @pytest.mark.skip(reason='Метод не работает.')
    def test_post_api_reports_id_download(self):
        body = {"Parameters": {"51": "38"}}
        # Формируем отчет
        request = self.APP.g1_api_reports.post_reports_id_download(5, body=body)
        assert request
        assert self.APP.group_data.response.status_code == 200