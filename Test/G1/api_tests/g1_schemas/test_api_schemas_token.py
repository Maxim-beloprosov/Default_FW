import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Токен.')
class TestApiSchemasToken(G1ApiBase):

    @allure.title('POST /Token')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_token(self):
        # Запрашиваем токен
        self.APP.api_token.get_token()
        assert self.APP.group_data.access_token
        assert self.APP.group_data.token_type
        assert self.APP.group_data.expires_in