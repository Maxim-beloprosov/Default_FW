import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Группы ответственности')
class TestApiSchemasResponsibilityGroups(G1ApiBase):

    @allure.title('GET api/ResponsibilityGroups/Id/Users')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_responsibility_groups_id_users(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()

        # Получаем норматив для поиска группы ответственности
        normative = self.APP.g1_api_work_normative.get_work_normative_search(params={'phrase': 'Тестовый_Тип_1', 'size': 20, 'page': 1, 'any': True})
        # Получаем группу ответственности для поиска пользователей ГО
        responsibility_group = self.APP.g1_api_work_normative.get_work_normative_id_responsibility_groups(normative[0]['Id'], params={'withUsers': False})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()

        # Получаем пользователей ГО
        request = self.APP.g1_api_responsibility_groups.get_responsibility_groups_id_users(responsibility_group[0]['Id'])
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Id' in request[0]
        assert 'UserNameWithStatus' in request[0]
        assert 'Region' in request[0]
