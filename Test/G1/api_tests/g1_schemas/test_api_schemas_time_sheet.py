import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. Табель времени')
class TestApiSchemasTask(G1ApiBase):

    @allure.title('GET api/TimeSheet/User')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_api_time_sheet_user(self):
        # получаем профиль текущего пользователя
        user = self.APP.g1_api_users.get_users_current()
        # получаем табель пользователя
        request = self.APP.g1_api_time_sheet.get_time_sheet_user(params={'userId': user['Id'], 'date': self.APP.time.get_time_now()})
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert request[0]['UserId'] == user['Id']
        assert request[0]['UserFullName'] == user['LastName'] + ' ' + user['FirstName']
        assert 'Period' in request[0]

    @allure.title('PUT api/TimeSheet/User')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_api_time_sheet_user(self):
        # получаем профиль текущего пользователя
        user = self.APP.g1_api_users.get_users_current()
        body = {
            'UserId': user['Id'],
            'DateStart': self.APP.time.get_date_increased_x_days_json(0),
            'DateEnd': self.APP.time.get_date_increased_x_days_json(1),
            'TimeBegin': 1,
            'TimeEnd': 100,
            'TimeSheetDayType': 4
        }

        # редактируем табель пользователя
        request = self.APP.g1_api_time_sheet.put_time_sheet_user(body)
        assert request
        assert self.APP.group_data.response.status_code == 200
        assert 'Data' in request
        assert 'Status' in request
