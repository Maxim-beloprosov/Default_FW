import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiTimeSheet(G1APIBase):

    @allure.step('Вернуть табель пользователя за указанную дату или интервал дат. GET api/TimeSheet/User')
    def get_time_sheet_user(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/TimeSheet/User', params)

    @allure.step('Редактирование табеля пользователя за указанную дату или интервал дат. PUT api/TimeSheet/User')
    def put_time_sheet_user(self, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/TimeSheet/User', body, params)
