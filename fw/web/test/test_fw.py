from selenium.webdriver.common.by import By
import allure
import time

from selenium.webdriver.common.devtools.v104.indexed_db import Key

from fw.web.web_base import WebBase


class Locator:
    input_search_block = (By.XPATH, '(//input)[1]')
    button_search = (By.XPATH, '//div[@class="lJ9FBc"]//input[1]')


class TestFW(WebBase):

    @allure.step('Вводим тест в поле поиска')
    def send_text_to_search_block(self, text):
        self.send_keys(Locator.input_search_block, text)

    @allure.step('Нажимаем кнопку поиска')
    def click_button_search(self):
        # Добавил тайм-аут, т.к. там прогружается анимация на результаты поиска
        time.sleep(1)
        self.click_element(Locator.button_search)


    @allure.step('Нажимаем на нужный сайт в результатах поиска гугла')
    def select_need_url_in_list_result(self, url):
        need_button = (By.XPATH, f'//cite[contains(text(),"{url}")]')
        self.click_element(need_button)

