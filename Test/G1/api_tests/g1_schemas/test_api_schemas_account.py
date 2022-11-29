import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Учетная запись пользователя.')
class TestApiSchemasAccount(G1ApiBase):

    @allure.title('POST api/Account/ConfirmRegistration')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_account_confirm_registration(self):
        # отправляем запрос
        request = self.APP.g1_api_account.post_account_confirm_registration(body={'Email': self.APP.group_data.g1_users['User5']['Email']})
        assert request
        assert self.APP.group_data.response.status_code == 200

    @allure.title('POST api/Account/Restore')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_account_restore(self):
        # отправляем запрос
        request = self.APP.g1_api_account.post_account_restore(body={'Email': self.APP.group_data.g1_users['User1']['Email']})
        assert request
        assert self.APP.group_data.response.status_code == 200