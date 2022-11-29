import allure
from selenium.webdriver.common.by import By

from fw.web.tickets.tickets_base import TicketsBase


class Locator:
    page_loaded = (By.XPATH, '//div[@class="async-wrapper-constructor-type-field-editor"]')


class TaskId(TicketsBase):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)
