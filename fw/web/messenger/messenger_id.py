import allure
from selenium.webdriver.common.by import By

from fw.web.AnyPage import AnyPage


class Locator:
    cke_contents = (By.XPATH, '//div[@class="chat-center-wrap"]')


class MessengerId(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)