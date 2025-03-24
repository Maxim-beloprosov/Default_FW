import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Test')
@allure.story('Тест')
class Test(ApiBase):

    @allure.title('Test')
    @pytest.mark.Test
    @pytest.mark.ApiTest
    def test(self):

        # Готовим данные для запроса
        test = 'test'
        # Отправляем запрос по нужному адресу
        request = self.APP.api_request.get_test(test)

        # Сравниваем значения с ожидаемыми значениями
        assert request['test'] == 'test'

