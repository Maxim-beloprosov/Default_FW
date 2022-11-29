import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Листы допуска.')
class TestApiSchemasAccessSheet(G1ApiBase):

    @allure.title('POST api/AccessSheet/Search')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_access_sheet_search(self):
        access_sheet_search = self.APP.g1_api_access_sheet.post_access_sheet_search(
            body={"ListType": 0, "Limits": {"Page": 1, "PageSize": 2}, "Order": {"Property": "CreateDate", "DirectionType": 0}})
        assert self.APP.group_data.response.status_code == 200
        assert 'Data' in access_sheet_search
        assert 'TotalCount' in access_sheet_search
        assert 'Limits' in access_sheet_search

    @allure.title('GET api/AccessSheet/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_access_sheet_id(self):
        access_sheet = self.APP.g1_api_access_sheet.get_access_sheet_id(id=1)
        assert self.APP.group_data.response.status_code == 200
        assert access_sheet['Id'] == 1
        assert 'Initiator' in access_sheet
        assert 'CreateDate' in access_sheet
        assert 'Status' in access_sheet
        assert 'CanRateRequests' in access_sheet
        assert 'TreeNodes' in access_sheet
