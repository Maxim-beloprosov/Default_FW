import time

import allure
import pytest

from Test.web_tests.web_base import WebBase


class Test(WebBase):

    @allure.title('Переходим на сайт Apple')
    @pytest.mark.WebTest
    def test_go_to_apple(self):
        # Вводим текст в поле поиска
        self.APP.test_fw.send_text_to_search_block('Сайт Apple')
        # Нажимаем кнопку поиска
        self.APP.test_fw.click_button_search()
        # Нажимаем на нужный сайт, который передаем
        correct_url = 'https://www.apple.com'
        self.APP.test_fw.select_need_url_in_list_result(correct_url)
        # Получаем ссылку сайта
        actual_url = self.APP.web_base.get_current_url()
        assert correct_url + '/' == actual_url